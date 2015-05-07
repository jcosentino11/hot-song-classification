# Usage: python convert_raw_to_csv.py <dataset> <outfile>

import os
import sys
sys.path.insert(0, '../util')
import logger as lg
import hdf5util as hdf5
import csvutil as csv

DATA_DIR = '../../data'
RAW_DATA_DIR = '../../raw-data'
TRAINING_DIR = os.path.join(RAW_DATA_DIR, 'A')
TEST_DIR = os.path.join(RAW_DATA_DIR, 'B')

def load_data_file(path):
	return hdf5.read_file(path)

def scrape_data_file(f):
	return hdf5.get_vals(f)

def scrape_raw_dataset(path):
	dataset = []
	for root, dirs, files in os.walk(path):
		for filename in files:
			if '.h5' in filename:
				lg.log(lg.V, 'Reading from %s' % filename)
				f = load_data_file(os.path.join(root, filename))
				row = scrape_data_file(f)
				lg.log(lg.V, row) 
				dataset.append(row)
	return dataset

def scrape_dataset(name):
	if name == 'test':
		return scrape_raw_dataset(TEST_DIR)
	elif name == 'training':
		return scrape_raw_dataset(TRAINING_DIR)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		lg.log(lg.E, 'Usage: python convert_raw_to_csv.py <dataset> <outfile>')
		sys.exit(1)
	dataset = scrape_dataset(sys.argv[1])
	csv.append_header(dataset)

	csv.write(dataset, os.path.join(DATA_DIR, sys.argv[2]))
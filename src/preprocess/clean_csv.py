#Usage: python clean_csv.py <infile>

import os
import sys
sys.path.insert(0, '../util')
import logger as lg
import csvutil as csv

COLS_TO_REMOVE = ['danceability']

DATA_DIR = '../../data'

def remove_empty_cols(filename):
	path = os.path.join(DATA_DIR, filename)
	dataset = csv.read(path)
	csv.remove_cols(COLS_TO_REMOVE, dataset)
	csv.write(dataset, path)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		lg.log(lg.E, 'Usage: python clean_csv.py <infile>')
		sys.exit(1)

	remove_empty_cols(sys.argv[1])
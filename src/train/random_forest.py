# Usage: python random_forest.py <trainingset> <testset> <outfile> <numtrees>

from sklearn.ensemble import RandomForestClassifier
import os
import sys
sys.path.insert(0, '../util')
import logger as lg
import csvutil as csv
from numpy import savetxt

DATA_DIR = '../../data'
removed_header = []

def load_data_from_csv(infile):
	return csv.read(os.path.join(DATA_DIR, infile))

def load_dataset(infile):
	dataset = load_data_from_csv(infile)
	remove_header(dataset)
	return dataset

def save_data_to_csv(dataset, outfile):
	csv.write(dataset, os.path.join(DATA_DIR, outfile))

def remove_header(dataset):
	global removed_header
	removed_header = dataset.pop(0)

def restore_header(dataset):
	if len(removed_header) > 0:
		dataset.insert(0, removed_header)
	return dataset

if __name__ == '__main__':
	if len(sys.argv) != 5:
		lg.log(lg.E, 'Usage: python random_forest.py <trainingset> <testset> <outfile> <numtrees>')
		sys.exit(1)

	trainingset = load_dataset(sys.argv[1])
	testset = load_dataset(sys.argv[2])

	targetindex = len(trainingset[0]) - 1

	target = [x[targetindex] for x in trainingset]
	train = [x[0:targetindex] for x in trainingset]

	rf = RandomForestClassifier(n_estimators=int(sys.argv[4]))
	rf.fit(train, target)

	testset = [x[:-1] for x in testset]
	resultset = rf.predict(testset)

	for i in xrange(len(testset)):
		testset[i].append(resultset[i])
	testset = restore_header(testset)
	save_data_to_csv(testset, sys.argv[3])

	# savetxt(os.path.join(DATA_DIR, sys.argv[3]), , delimiter=',', fmt='%f')

	
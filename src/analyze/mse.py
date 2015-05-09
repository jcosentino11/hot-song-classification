# Usage: mse.py <testset> <predictionset> <outfile>

import os
import sys
sys.path.insert(0, '../util')
import csvutil as csv

DATA_DIR = '../../data'

def load_data_from_csv(infile):
	return csv.read(os.path.join(DATA_DIR, infile))

def mse(y, yhat):
	s = 0
	for i in xrange(len(y)):
		s += (yhat[i] - y[i]) ** 2
	return s / len(y)

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print('Usage: mse.py <testset> <predictionset> <outfile>')
		sys.exit(1)

	testset = load_data_from_csv(sys.argv[1])
	predictionset = load_data_from_csv(sys.argv[2])

	testtarget = [float(x[-1]) for x in testset[1:]]
	predictiontarget = [float(x[-1]) for x in predictionset[1:]]

	error = mse(testtarget, predictiontarget)

	print("MSE: %f" % error)

	with open(os.path.join(DATA_DIR, sys.argv[3]), 'a') as f:
		f.write("MSE: %f\n" % error)
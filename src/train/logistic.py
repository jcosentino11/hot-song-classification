# Usage: python logistic.py <trainingset> <testset> <outfile>

import os
import sys

from sklearn.linear_model import LogisticRegression

sys.path.insert(0, '../util')
from dm import DatasetManager

DATA_DIR = '../../data'

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print('Usage: python logistic.py <trainingset> <testset> <outfile>')
		sys.exit(1)

	# setup file paths
	trainingpath = os.path.join(DATA_DIR, sys.argv[1])
	testpath = os.path.join(DATA_DIR, sys.argv[2])
	resultpath = os.path.join(DATA_DIR, sys.argv[3])

	# create managers and load datasets
	traindm = DatasetManager(inpath=trainingpath)
	traindm.load().remove_header()
	testdm = DatasetManager(inpath=testpath)
	testdm.load().remove_header()

	# isolate target col from training set
	targetindex = len(traindm.dataset[0]) - 1
	target = [x[targetindex] for x in traindm.dataset]
	train = [x[0:targetindex] for x in traindm.dataset]

	# fit the logistic regression
	dt = LogisticRegression()
	dt.fit(train, target)
	
	# make predictions on test set
	testdm.remove_col_by_index(-1)
	results = dt.predict(testdm.dataset)

	# save results to disk
	result = DatasetManager.from_dm(testdm)
	result.append_col(results)
	result.restore_header()
	result.outpath = resultpath
	result.save()
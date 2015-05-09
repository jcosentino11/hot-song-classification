# Usage: python random_forest.py <trainingset> <testset> <outfile> <numtrees>

from sklearn.ensemble import RandomForestClassifier
import copy
import os
import sys
sys.path.insert(0, '../util')
from dm import DatasetManager

DATA_DIR = '../../data'

if __name__ == '__main__':
	if len(sys.argv) != 5:
		print('Usage: python random_forest.py <trainingset> <testset> <outfile> <numtrees>')
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

	# build the forest
	rf = RandomForestClassifier(n_estimators=int(sys.argv[4]), random_state=1)
	rf.fit(train, target)

	# make predictions on test set
	testdm.remove_col_by_index(-1)
	results = rf.predict(testdm.dataset)

	# save results to disk
	result = DatasetManager.from_dm(testdm)
	result.append_col(results)
	result.restore_header()
	result.outpath = resultpath
	result.save()
# Usage: python decision_tree.py <trainingset> <testset> <outfile> <viz>

import os
import sys

from sklearn import tree

sys.path.insert(0, '../util')
from dm import DatasetManager

DATA_DIR = '../../data'

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print('Usage: python decision_tree.py <trainingset> <testset> <outfile> <viz>')
		sys.exit(1)

	# setup file paths
	trainingpath = os.path.join(DATA_DIR, sys.argv[1])
	testpath = os.path.join(DATA_DIR, sys.argv[2])
	resultpath = os.path.join(DATA_DIR, sys.argv[3])
	featpath = os.path.join(DATA_DIR, 'tree/importances.csv')

	# create managers and load datasets
	traindm = DatasetManager(inpath=trainingpath)
	traindm.load().remove_header()
	testdm = DatasetManager(inpath=testpath)
	testdm.load().remove_header()

	# isolate target col from training set
	targetindex = len(traindm.dataset[0]) - 1
	target = [x[targetindex] for x in traindm.dataset]
	train = [x[0:targetindex] for x in traindm.dataset]

	# build the tree
	dt = tree.DecisionTreeClassifier()
	dt.fit(train, target)

	# print tree info
	print("num classes: %d" % dt.n_classes_)

	# make predictions on test set
	testdm.remove_col_by_index(-1)
	results = dt.predict(testdm.dataset)

	# save results to disk
	result = DatasetManager.from_dm(testdm)
	result.append_col(results)
	result.restore_header()
	result.outpath = resultpath
	result.save()

	# save feat importance to disk
	feat = []
	feat.append(result.dataset[0])
	feat.append(dt.feature_importances_)
	featdm = DatasetManager.from_dataset(feat)
	featdm.outpath = featpath
	featdm.save()

	# generate visualization
	if len(sys.argv) == 5:
		tree.export_graphviz(dt, out_file='./../../data/tree/tree.dot')
#!/usr/bin/python

import os
import sys

from pylab import *

from dm import DatasetManager

DATA_DIR = './../../data'

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: python decision_tree.py <dataset>')
		sys.exit(1)

	# setup file paths
	path = os.path.join(DATA_DIR, sys.argv[1])

	# create managers and load dataset
	dm = DatasetManager(inpath=path)
	dm.load().remove_header()

	for i in xrange(len(dm.dataset[0])):
		figure(i)
		boxplot(dm.get_col(i))
		title(dm.header[i])
		xticks(range(1),'')
	show()
	
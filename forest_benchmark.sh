#!/bin/bash
cd ./src/train

SIZES="1 2 3 4 5 6 7 8 9 10"

for size in $SIZES
do
	python random_forest.py training.csv test.csv forestpred.csv $size
	cd ./../analyze
	echo "Size: $size"
	python mse.py test.csv forestpred.csv forestresults.txt
	cd ./../train
done
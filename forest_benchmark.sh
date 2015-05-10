#!/bin/bash
echo "Starting Forest Benchmark"
cd ./src/train/
for ((i=1; i<=50; i++))
do
	python random_forest.py training.csv test.csv forest/forestpred.csv 1
	cd ./../analyze
	echo "Size: 1"
	python mse.py test.csv forest/forestpred.csv forest/forestresults.txt
	cd ./../train
done
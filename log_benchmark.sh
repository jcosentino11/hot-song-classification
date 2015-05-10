#!/bin/bash
cd ./src/train/
echo "Starting Logistic Benchmark"
for ((i=1; i<=1; i++))
do
	python logistic.py training.csv test.csv logistic/logpred.csv
	cd ./../analyze
	python mse.py test.csv logistic/logpred.csv logistic/logresults.txt
	cd ./../train
done
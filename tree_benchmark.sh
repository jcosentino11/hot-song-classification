#!/bin/bash
cd ./src/train/
echo "Starting Tree Benchmark"
for ((i=1; i<=5; i++))
do
	python decision_tree.py training.csv test.csv tree/treepred.csv
	cd ./../analyze
	python mse.py test.csv tree/treepred.csv tree/treeresults.txt
	cd ./../train
done
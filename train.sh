#!/bin/bash
cd ./src/train
echo "Training random forest of size $1"
python random_forest.py training.csv test.csv forestpred.csv $1
echo "Done."
#!/bin/bash
cd ./src/analyze
echo "Calculating random forest mean squared error..."
python mse.py test.csv forestpred.csv results.txt
echo "Done."
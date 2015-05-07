#!/bin/bash
cd ./src/preprocess
echo "Converting raw data to csv format..."
python convert_raw_to_csv.py training training.csv
python convert_raw_to_csv.py test test.csv
echo "Done."
echo "Cleaning csv data..."
python clean_csv.py training.csv training.csv
python clean_csv.py test.csv test.csv
echo "Done. files located in 'data' directory"
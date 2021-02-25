#!/bin/bash

main=main_v0.py
echo "Running all for $main"

python3 $main 1
python3 $main 2
python3 $main 3
python3 $main 4
python3 $main 5
python3 $main 6

echo "DONE"

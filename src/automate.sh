#!/usr/bin/env bash

# Building 

while read -r link num name; do
  echo "Creating video for: $link"
  python3 run.py $link $num $name
done <"list.txt"


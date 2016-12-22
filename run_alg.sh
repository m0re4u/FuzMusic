#!/bin/bash

# Run from this project's root directory(typically FuzMusic/)

# Get tags from all files in a directory with some default settings
if [[ -z $1 ]]; then
  echo "[!] Please specify a directory"
elif [[ -z $2 ]] && [[ -n $1 ]]; then
  echo "[!] Reading in jsons from $1"
  echo "[!] Please input new pickle filename(.pik): "
  read PICKLEFILE
  python preprocess/get_tags_from_jsonfiles.py $1 $PICKLEFILE --limit 100
  echo "[!] Extracted all tags"
  echo "[!] Running clustering algorithm"
  python eval/predict_user.py "$1" "$PICKLEFILE" preprocessed_data/test/user_000001.json
fi

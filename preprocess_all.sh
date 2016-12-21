#!/bin/bash

# Run from this project's root directory(typically FuzMusic/)

# Get tags from all files in a directory with some default settings
if [[ -z $1 ]]; then
  echo "[!] Please specify a directory"
elif [[ -z $2 ]] && [[ -n $1 ]]; then
  echo "[!] Preprocessing user data "
  FILES="$1*.tsv"
  for f in $FILES; do
    echo "[!] Processing $f"
    python preprocess/get_tags_from_artists.py --limit 10 $f
  done
  echo "[!] Done preprocessing user data"
fi

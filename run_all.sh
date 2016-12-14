#!/bin/bash

if [[ -z $1 ]]; then
  echo "Please specify a directory!"
elif [[ -z $2 ]] && [[ -n $1 ]]; then
  FILES="$1*.txt"
  for f in $FILES; do
    echo "Processing $f"
    python data-handling/get_tags_from_artists.py --no-ones $f
  done
fi

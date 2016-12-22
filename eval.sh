#! /bin/bash

echo "Running static baseline"
python eval/eval_static.py ~/data/lastfm-dataset-1K/split/test/ all_100.pik --limit 100

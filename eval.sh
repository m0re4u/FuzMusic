#! /bin/bash
echo "Running static baseline"
python eval/eval_static.py preprocessed_data/test/ all_100.pik --limit 100
echo "Running kmeans with k=36-49, limit=100, method='dot'"
python eval/eval_per_ck.py preprocessed_data/train/ preprocessed_data/test/ all_100.pik 36 49 --limit 100 --method dot --use_k
echo "Running cmeans with c=36-49, limit=100, method='dot'"
python eval/eval_per_ck.py preprocessed_data/train/ preprocessed_data/test/ all_100.pik 36 49 --limit 100 --method dot

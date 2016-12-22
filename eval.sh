#! /bin/bash
echo "Running static baseline, method=dot"
python eval/eval_static.py preprocessed_data/test/ all_100.pik --limit 100
echo "Running static baseline, method=euclidean"
python eval/eval_static.py preprocessed_data/test/ all_100.pik --limit 100 --method eucl
echo "Running kmeans with k=36-49, limit=100, method='dot'"
python eval/eval_per_ck.py preprocessed_data/train/ preprocessed_data/test/ all_100.pik 36 49 --limit 100 --method dot --use_k
echo "Running kmeans with k=36-49, limit=100, method='euclidean'"
python eval/eval_per_ck.py preprocessed_data/train/ preprocessed_data/test/ all_100.pik 36 49 --limit 100 --method eucl --use_k
echo "Running cmeans with c=38-43, limit=100, method='dot'"
python eval/eval_per_ck.py preprocessed_data/train/ preprocessed_data/test/ all_100.pik 36 43 --limit 100 --method dot
echo "Running cmeans with c=38-43, limit=100, method='euclidean'"
python eval/eval_per_ck.py preprocessed_data/train/ preprocessed_data/test/ all_100.pik 36 43 --limit 100 --method eucl

#! /bin/bash

# Predict an album to a single user
python eval/predict_user.py preprocessed_data/train/ all_100.pik preprocessed_data/test/user_000001.json

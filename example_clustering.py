import argparse
import skfuzzy as fuzz
import numpy as np
import preprocess.make_user_vectors as muv


def main(train_data, all_tags):
    # Create vectors for all users and put them in a big matrix of shape
    # S x N, where S is the number of features in a vector, and there are N
    # data points in S-dimensional space.
    print("Creating user vectors")
    train = muv.make_vectors(train_data, all_tags)
    print(train.shape)

    # Run cmeans, usage:
    # https://github.com/scikit-fuzzy/scikit-fuzzy/blob/master/skfuzzy/cluster/_cmeans.py
    # cntr, U, U0, d, Jm, p, fpc = fuzz.cluster.cmeans(
    print("Running cmeans clustering.")
    results = fuzz.cluster.cmeans(
        train, 6, 2., error=0.005, maxiter=1000, init=None)

    print("=== Done! ===")
    print("fpc: {}".format(results[6]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create clusters of users\
    based on the tags they listen to.')
    parser.add_argument('folder', help='Folder with user tag data(jsons)')
    parser.add_argument('all_tags', help='Pickle file containing the tag list')
    args = parser.parse_args()
    main(args.folder, args.all_tags)

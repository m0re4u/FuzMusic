import argparse
import skfuzzy as fuzz
import numpy as np
import preprocess.make_user_vectors as muv
import defuzz.defuzz_fclusters as defuzz


def predict_user(clusters, uservec):
    res = fuzz.cluster.cmeans_predict(uservec, clusters)
    print(res)


def main(train_data, all_tags, userfile):
    # Create vectors for all users and put them in a big matrix of shape
    # S x N, where S is the number of features in a vector, and there are N
    # data points in S-dimensional space.
    print("Creating user vectors")
    train = muv.make_vectors(train_data, all_tags)
    print(train.shape)

    # Run cmeans, usage:
    # https://github.com/scikit-fuzzy/scikit-fuzzy/blob/master/skfuzzy/cluster/_cmeans.py
    print("Running cmeans clustering.")
    results = fuzz.cluster.cmeans(
        train, 6, 2., error=0.005, maxiter=1000, init=None)

    print("=== Done! ===")
    print("fpc: {}".format(results[6]))

    # Predict the memberships to the different clusters for a new user
    print("Creating new user vector")
    udata = muv.make_vector(userfile, all_tags)
    print(udata.shape)
    print("Predicting user cluster memberships")
    ures = fuzz.cluster.cmeans_predict(udata, results[0], 2., 0.005, 1000)
    # Defuzzify the clusters and their memberships into one single vector
    newvec = defuzz.combine_fclusters(results[0], ures[0])
    print(newvec)
    print(newvec.shape)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create clusters of users\
    based on the tags they listen to.')
    parser.add_argument('folder', help='Folder with user tag data(jsons)')
    parser.add_argument('all_tags', help='Pickle file containing the tag list')
    parser.add_argument('user', help='new user to predict')
    args = parser.parse_args()
    main(args.folder, args.all_tags, args.user)

import os
import json
import glob
import argparse
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import eval.measures as measures
import defuzz.get_highest_tag as gh
import defuzz.defuzz_fclusters as defuzz
import defuzz.get_top_album_from_tag as tgal
import preprocess.make_user_vectors as muv
from sklearn.cluster import KMeans


def evaluate_cmeans(train_data, test_data, all_tags, limit, clusters=6,
                    method='dot'):

    # Cluster training data
    print("Clustering(cmeans) with {} clusters, measuring performance with {}\
    ".format(clusters, method))
    train = muv.make_vectors(train_data, all_tags, limit)
    results = fuzz.cluster.cmeans(
        train, clusters, 2., error=0.005, maxiter=1000, init=None)

    # Test on all test files
    files = glob.glob(os.path.join(test_data, "*.json"))
    p = []
    print("Testing on {} files".format(len(files)))
    for f in files:
        print(".", end="", flush=True)
        # Predict the cluster and membership for new user
        udata = muv.make_vector(f, all_tags, limit)
        ures = fuzz.cluster.cmeans_predict(udata, results[0], 2., 0.005, 300)
        # Defuzzify
        newvec = defuzz.combine_fclusters(results[0], ures[0])
        uvec = np.squeeze(np.asarray(udata))
        best_tag = gh.highest_tag(newvec, uvec, all_tags)

        # Return album based on defuzzification
        secretfile = '.api_key'
        with open(secretfile) as f:
            lastfm = json.load(f)
        album_name, album_vec = tgal.get_top_album(
            lastfm, best_tag[0], all_tags)

        # Show performance
        if method == 'eucl':
            perf = measures.euclidean_dist(album_vec, uvec)
            print(perf)
        else:
            perf = measures.dot_product(album_vec, uvec)
        # print("Performance: {}".format(perf))
        p.append(perf)
    return p


def evaluate_kmeans(train_data, test_data, all_tags, limit=100, clusters=6,
                    method='dot'):
    # Cluster training data
    print("Clustering(kmeans) with {} clusters".format(clusters))
    train = muv.make_vectors(train_data, all_tags, limit)
    c = KMeans(clusters, max_iter=300, init='random')
    c.fit(train)

    # Test on all test files
    files = glob.glob(os.path.join(test_data, "*.json"))
    p = []
    print("Testing on {} files".format(len(files)))
    for f in files:
        print(".", end="", flush=True)
        # Predict the cluster and membership for new user
        udata = muv.make_vector(f, all_tags, limit)
        ures = c.fit_predict(udata)
        # Defuzzify
        uvec = np.squeeze(np.asarray(udata))
        ures = np.squeeze(np.asarray(ures))
        best_tag = gh.highest_tag(ures, uvec, all_tags)

        # Return album based on defuzzification
        secretfile = '.api_key'
        with open(secretfile) as f:
            lastfm = json.load(f)
        album_name, album_vec = tgal.get_top_album(
            lastfm, best_tag[0], all_tags)

        # Show performance
        if method == 'eucl':
            perf = measures.euclidean_dist(album_vec, uvec)
        else:
            perf = measures.dot_product(album_vec, uvec)

        p.append(perf)
    return p


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test performance of cmeans')
    parser.add_argument('train', help='Folder with user tag data(jsons) to \
    find clusters')
    parser.add_argument('test', help='Folder with user tag data(jsons) as \
    testing data')
    parser.add_argument('all_tags', help='Pickle file containing the tag list')
    parser.add_argument('--limit', dest='limit', type=int, metavar='N',
                        help='Only use tags with more than N occurrences',
                        default=100)
    args = parser.parse_args()
    print("Doing k-means")
    rk = evaluate_kmeans(args.train, args.test, args.all_tags, args.limit)
    print("Doing c-means")
    rc = evaluate_cmeans(args.train, args.test, args.all_tags, args.limit)
    plt.plot(rk)
    plt.plot(rc)
    plt.ylim((0, 1))
    plt.show()
    print(rk)
    print(rc)
    print(np.std(rk))
    print(np.std(rc))

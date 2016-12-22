import json
import argparse
import skfuzzy as fuzz
import numpy as np
import preprocess.make_user_vectors as muv
import defuzz.defuzz_fclusters as defuzz
import defuzz.get_highest_tag as gh
import defuzz.get_top_album_from_tag as tgal
import eval.measures as measures


def predict_user(clusters, uservec):
    res = fuzz.cluster.cmeans_predict(uservec, clusters)
    print(res)


def main(train_data, all_tags, userfile, limit):
    # Create vectors for all users and put them in a big matrix of shape
    # S x N, where S is the number of features in a vector, and there are N
    # data points in S-dimensional space.
    print("Creating user vectors")
    train = muv.make_vectors(train_data, all_tags, limit)

    # Run cmeans, usage:
    # https://github.com/scikit-fuzzy/scikit-fuzzy/blob/master/skfuzzy/cluster/_cmeans.py
    print("Running cmeans clustering.")
    results = fuzz.cluster.cmeans(
        train, 6, 2., error=0.005, maxiter=1000, init=None)
    print("Done clustering")

    # Predict the memberships to the different clusters for a new user
    print("Creating new user vector")
    udata = muv.make_vector(userfile, all_tags, limit)
    print("Predicting user cluster memberships")

    ures = fuzz.cluster.cmeans_predict(udata, results[0], 2., 0.005, 1000)
    # Defuzzify the clusters and their memberships into one single vector
    newvec = defuzz.combine_fclusters(results[0], ures[0])
    # user data as an np array, not a matrix:
    uvec = np.squeeze(np.asarray(udata))

    # Highest scoring tag in difference
    best_tag = gh.highest_tag(newvec, uvec, all_tags)
    print("Highest tag was: {} with score {}".format(best_tag[0], best_tag[1]))

    # Default location, lots of stuff breaks if this isn't there
    secretfile = '.api_key'
    with open(secretfile) as f:
        lastfm = json.load(f)
    album_name, album_vec = tgal.get_top_album(lastfm, best_tag[0], all_tags)
    print("Recommend album: {}".format(album_name))
    print(album_vec.shape)
    # Performance of run
    perf = measures.dot_product(album_vec, uvec)
    print("Performance: {}".format(perf))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create clusters of users\
    based on the tags they listen to.')
    parser.add_argument('folder', help='Folder with user tag data(jsons)')
    parser.add_argument('all_tags', help='Pickle file containing the tag list')
    parser.add_argument('user', help='new user to predict')
    parser.add_argument('--limit', dest='limit', type=int, metavar='N',
                        help='Only use tags with more than N occurrences',
                        default=100)
    args = parser.parse_args()
    main(args.folder, args.all_tags, args.user, args.limit)

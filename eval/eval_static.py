import os
import json
import glob
import pylast
import argparse
import numpy as np
import preprocess.make_user_vectors as muv
import eval.measures as measures
import defuzz.get_top_album_from_tag as tgal


def get_static_album(api_data, pikfile):
    # Connect to Last.fm API
    # For usage of the pylast package, type help(pylast) after importing
    password_hash = pylast.md5(api_data['password'])
    network = pylast.LastFMNetwork(
        api_key=api_data['key'],
        api_secret=api_data['shared_secret'],
        username=api_data['username'],
        password_hash=password_hash)

    # Get the information from lastfm servers
    try:
        default_album = pylast.Album("Metallica", "Death Magnetic", network)
        albumTTags = default_album.get_top_tags(limit=250)

        # Make a vector from the album
        albumVec = tgal.get_album_vector(albumTTags, pikfile)
        return (str(default_album), albumVec)

    except Exception as e:
        print("Something went wrong. Maybe the input arguments are \
        incompatible. The error message is:")
        print(e)


def evaluate_static(test_data, all_tags, limit):

    # Cluster training data
    print("Evaluating static baseline")
    secretfile = '.api_key'
    with open(secretfile) as f:
        lastfm = json.load(f)
    album_name, album_vec = get_static_album(lastfm, all_tags)

    files = glob.glob(os.path.join(test_data, "*.json"))
    p = []
    print("Testing on {} files".format(len(files)))
    for f in files:
        print(".", end="", flush=True)
        # Predict the cluster and membership for new user
        udata = muv.make_vector(f, all_tags, limit)
        uvec = np.squeeze(np.asarray(udata))
        # Show performance
        perf = measures.dot_product(album_vec, uvec)
        # print("Performance: {}".format(perf))
        p.append(perf)
    return p

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test performance of cmeans')
    parser.add_argument('test', help='Folder with user tag data(jsons) as \
    testing data')
    parser.add_argument('all_tags', help='Pickle file containing the tag list')
    parser.add_argument('--limit', dest='limit', type=int, metavar='N',
                        help='Only use tags with more than N occurrences',
                        default=100)
    args = parser.parse_args()

    res = evaluate_static(args.test, args.all_tags, args.limit)
    nl = np.array(res)
    print()
    print("{} clusters: mu {}: std: {}".format(nl.shape, np.mean(nl), np.std(nl)))

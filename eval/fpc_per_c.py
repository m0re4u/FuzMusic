import argparse
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import preprocess.make_user_vectors as muv


def main(train_data, all_tags, maxc):
    fpcs = []
    for i in range(2, maxc):
        train = muv.make_vectors(train_data, all_tags)

        results = fuzz.cluster.cmeans(
            train, i, 2., error=0.010, maxiter=300, init=None)

        fpcs.append(results[6])
        print("Trained {}, {}".format(i, results[6]))

    plt.plot(np.r_[2:maxc], fpcs)
    plt.xlabel("Number of clusters")
    plt.ylabel("fpc")
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create clusters of users\
    based on the tags they listen to.')
    parser.add_argument('folder', help='Folder with user tag data(jsons) for \
    clustering')
    parser.add_argument('all_tags', help='Pickle file containing the tag list')
    parser.add_argument('maxc', help='Maximum number of clusters to try. Will\
    train models with up to this number of clusters')
    args = parser.parse_args()
    main(args.folder, args.all_tags, args.maxc)

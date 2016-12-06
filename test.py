import skfuzzy as fuzz
import numpy as np


def main(bigdatafile):
    with open(bigdatafile, 'rb') as f:
        # Just to show the data was loaded in. Put a for loop here iterating
        # over the lines in the bigdatafile if you want to see what it look
        # like
        print("Loaded {}".format(bigdatafile))

        # Contains an example for cmeans for now, not sure how we model the
        # input vectors yet. This could be in the form of a vector with a '1'
        # for each tag(would create very large vectors but also prunable), or
        # we an use word2vec

        # https://github.com/scikit-fuzzy/scikit-fuzzy/blob/master/skfuzzy/cluster/_cmeans.py
        # Set random seed
        np.random.seed(42)

        # Generate pseudo-random reasonably well distinguished clusters
        xpts = np.zeros(0)
        ypts = np.zeros(0)

        x_corr = [7, 1, 4]
        y_corr = [3, 2, 1]

        for x, y, in zip(x_corr, y_corr):
            xpts = np.concatenate((xpts, np.r_[np.random.normal(x, 0.5, 200)]))
            ypts = np.concatenate((ypts, np.r_[np.random.normal(y, 0.5, 200)]))

        # Combine into a feature array
        features = np.c_[xpts, ypts].T
        print(np.size(features))
        print(features)

        # Usage:
        cntr, U, U0, d, Jm, p, fpc = fuzz.cluster.cmeans(
            features, 3, 2., error=0.005, maxiter=1000, init=None)

        print(cntr)


if __name__ == '__main__':
    # Path to the dataset, see:
    # http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/lastfm-1K.html
    # The file inserted here is an already extracted file, change it to your
    # own
    main("/home/m0re/data/lastfm-dataset-1K/userid-timestamp-artid-artname-traid-traname.tsv")

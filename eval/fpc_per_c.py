import argparse
import skfuzzy as fuzz
import preprocess.make_user_vectors as muv
import matplotlib.pyplot as plt


def main(train_data, all_tags):
    fpcs = []
    for i in range(0, 15):
        train = muv.make_vectors(train_data, all_tags)

        results = fuzz.cluster.cmeans(
            train, 4, 2., error=0.005, maxiter=1000, init=None)

        fpcs.append(results[6])

    plt.plot(np.r_[0:15], fpcs)
    plt.set_xlabel("Number of centers")
    plt.set_ylabel("Fuzzy partition coefficient")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create clusters of users\
    based on the tags they listen to.')
    parser.add_argument('folder', help='Folder with user tag data(jsons)')
    parser.add_argument('all_tags', help='Pickle file containing the tag list')
    args = parser.parse_args()
    main(args.folder, args.all_tags)

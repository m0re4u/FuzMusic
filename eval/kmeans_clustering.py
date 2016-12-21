import argparse
import preprocess.make_user_vectors as muv


def main(train_data, all_tags):
    fpcs = []
    for i in range(2, 30):
        print("Training {}".format(i))
        train = muv.make_vectors(train_data, all_tags)

        c = KMeans(i, max_iter=300)
        c.fit(train)

    print("Done!")
    print(c.cluster_centers_)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create clusters of users\
    based on the tags they listen to.')
    parser.add_argument('folder', help='Folder with user tag data(jsons)')
    parser.add_argument('all_tags', help='Pickle file containing the tag list')
    args = parser.parse_args()
    main(args.folder, args.all_tags)

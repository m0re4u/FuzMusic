import argparse
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import eval.eval_clustering as ec


def main(train, test, all_tags, mink, maxk, limit, use_k=False, method='dot'):
    means = []
    stds = []
    for i in range(mink, maxk):
        if use_k:
            res = ec.evaluate_kmeans(train, test, all_tags, limit, i, method)
        else:
            res = ec.evaluate_cmeans(train, test, all_tags, limit, i, method)
        mean = np.mean(np.array(res))
        std = np.std(np.array(res))
        means.append(mean)
        stds.append(std)
        print("Trained {}, mean:{}, std: {}".format(i, mean, std))

    plt.errorbar(np.r_[mink:maxk], means, stds, marker='^')
    plt.xlabel("Number of clusters")
    plt.ylabel("avg cosine_similarity")
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create clusters of users\
    based on the tags they listen to.')
    parser.add_argument('train', help='Folder with user tag data(jsons) to \
    find clusters')
    parser.add_argument('test', help='Folder with user tag data(jsons) as \
    testing data')
    parser.add_argument('all_tags', help='Pickle file containing the tag list')
    parser.add_argument('mink', help='minimum number of clusters to try. Will\
    train models with up to this number of clusters', type=int)
    parser.add_argument('maxk', help='Maximum number of clusters to try. Will\
    train models with up to this number of clusters', type=int)
    parser.add_argument('--use_k', dest='use_k', help='Force use of kmeans',
                        action='store_true', default=False)
    parser.add_argument('--limit', dest='limit', type=int, metavar='N',
                        help='Only use tags with more than N occurrences',
                        default=100)
    parser.add_argument('--method', dest='method', metavar='M',
                        help='Performance measuring method to use, defaults to\
                        cosine similarity', default='dot')
    args = parser.parse_args()
    main(
        args.train, args.test, args.all_tags, args.mink, args.maxk,
        args.limit, args.use_k, args.method)

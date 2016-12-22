import argparse
import numpy as np
import eval.eval_clustering as ec


def find_k(train, test, all_tags, limit, maxk):
    for i in range(21, maxk, 5):
        res = ec.evaluate_cmeans(train, test, all_tags, limit, i)
        nl = np.array(res)
        print("{} clusters: mu {}: std: {}".format(nl.shape, np.mean(nl), np.std(nl)))


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
    parser.add_argument('--maxk', dest='maxk', type=int, metavar='N',
                        help='Test with up to N clusters',
                        default=15)
    args = parser.parse_args()
    print("Doing c-means")
    find_k(args.train, args.test, args.all_tags, args.limit, args.maxk)

import os
import json
import glob
import argparse
import pickle
import numpy as np


def open_all_tags(filename):
    with open(filename, "rb") as infile:
        # Actually a dict
        tag_list = pickle.load(infile)
    return tag_list


def make_vectors(data_folder, all_tagsfile):
    files = glob.glob(os.path.join(data_folder, "*.json"))
    tag_list = open_all_tags(all_tagsfile)
    #
    vec = np.zeros((len(tag_list), 1))
    for f in files:
        with open(f, "r") as inf:
            small_list = json.load(inf)
        data = []
        for tag in tag_list:
            if tag in small_list.keys():
                data.append(small_list[tag])
            else:
                data.append(0)
        vec = np.c_[vec, np.array(data)]

    return vec


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make a vector out of a user\
     based on taglist')
    parser.add_argument('folder', help='folder with json files')
    parser.add_argument('all_tags', help='pickle(.pik) file containing all\
    tags')
    args = parser.parse_args()
    make_vectors(args.folder, args.all_tags)

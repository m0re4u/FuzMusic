import os
import json
import glob
import argparse
import pickle
import numpy as np


def open_all_tags(filename):
    """Open a pickle file to read in a list of all tags"""
    with open(filename, "rb") as infile:
        # Actually a dict
        tag_list = pickle.load(infile)
    return tag_list


def make_vectors(data_folder, all_tagsfile, min_count=10):
    """
    For every file in a directory, make a user file into a matrix with columns
    as tag count vectors
    """
    files = glob.glob(os.path.join(data_folder, "*.json"))
    tag_list = open_all_tags(all_tagsfile)
    vec = np.zeros((len(tag_list), 1))
    for f in files:
        uvec = _make_vector(f, all_tagsfile, min_count)
        vec = np.c_[vec, uvec]

    return vec[:, 1:]


def make_vector(userfile, all_tagsfile, min_count=10):
    """
    Transform a given user file into a matrix with one column
    """
    tag_list = open_all_tags(all_tagsfile)
    vec = np.zeros((len(tag_list), 1))
    uvec = _make_vector(userfile, all_tagsfile, min_count)
    vec = np.c_[vec, uvec]
    return vec[:, 1:]


def _make_vector(userfile, all_tagsfile, min_count=10):
    """
    Transform a given user file into a vector of tag counts
    """
    tag_list = open_all_tags(all_tagsfile)
    with open(userfile, "r") as uf:
        small_list = json.load(uf)
        # Minimum count of tags
        small_list = {k: v for k, v in small_list.items() if v > min_count}
    data = []
    for tag in tag_list:
        if tag in small_list.keys():
            data.append(small_list[tag])
        else:
            data.append(0)
    return np.array(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make a vector out of a user\
    based on taglist')
    parser.add_argument('folder', help='folder with json files')
    parser.add_argument('all_tags', help='pickle(.pik) file containing all\
    tags')
    parser.add_argument('--limit', dest='limit', type=int, metavar='N',
                        help='Only store tags with more than N occurrences',
                        default=10)
    args = parser.parse_args()
    make_vectors(args.folder, args.all_tags, args.limit)

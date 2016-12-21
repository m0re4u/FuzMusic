import os
import json
import glob
import argparse
import pickle


def main(folder, pikfile, limit=10):
    files = glob.glob(os.path.join(folder, "*.json"))

    global allTags  # Used to save all unique tags that were found
    allTags = []

    for jsonfile in files:
        print("Extracting {}".format(jsonfile))
        append_tags(jsonfile, limit)

    with open(pikfile, 'wb') as newFile:
        print("Storing {} tags in: {}".format(len(allTags), pikfile))
        pickle.dump(allTags, newFile)


def append_tags(jsonfile, limit=10):
    global allTags
    with open(jsonfile, 'r') as json_data:
        tags = json.load(json_data)
        for tag in tags:
            if tag not in allTags and tags[tag] > limit:
                allTags.append(tag)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make list of tags')
    parser.add_argument('folder', help='folder with json files')
    parser.add_argument('pikfile', help='Pickle file that will contain the tag\
    list')
    parser.add_argument('--limit', dest='limit', type=int, metavar='N',
                        help='Only store tags with more than N occurrences',
                        default=10)
    args = parser.parse_args()
    main(args.folder, args.pikfile, args.limit)

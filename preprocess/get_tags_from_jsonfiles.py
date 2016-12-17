import os
import json
import glob
import argparse
import pickle


def main(folder, pikfile):
    files = glob.glob(os.path.join(folder, "*.json"))

    global allTags  # Used to save all unique tags that were found
    allTags = []

    for jsonfile in files:
        print("Extracting {}".format(jsonfile))
        append_tags(jsonfile)

    with open(pikfile, 'wb') as newFile:
        print("Storing tags in: {}".format(pikfile))
        pickle.dump(allTags, newFile)


def append_tags(jsonfile):
    global allTags
    with open(jsonfile, 'r') as json_data:
        tags = json.load(json_data)
        for tag in tags:
            if tag not in allTags:
                allTags.append(tag)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make list of tags')
    parser.add_argument('folder', help='folder with json files')
    parser.add_argument('pikfile', help='Pickle file that will contain the tag\
    list')
    args = parser.parse_args()
    main(args.folder, args.pikfile)

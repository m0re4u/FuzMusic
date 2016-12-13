import os
import json
import argparse
import glob

def main(folder):
    jsonfilespath = folder + '\*.json'
    files = glob.glob(jsonfilespath)

    global allTags #Used to save all unique tags that were found
    allTags = []

    for jsonfile in files:
        append_tags(jsonfile)

    newFileName = 'all_tags.json'
    with open(newFileName,'w') as newFile :
        json.dump({'tag_list':allTags},newFile)

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
    args = parser.parse_args()
    main(args.folder)

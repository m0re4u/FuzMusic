import pylast
import json
import argparse
import numpy as np
import pickle


def open_all_tags(filename):
    """Open a pickle file to read in a list of all tags"""
    with open(filename, "rb") as infile:
        # Actually a dict
        tag_list = pickle.load(infile)
    return tag_list


def get_top_album(api_data, lfmTag, pikfile):
    # Connect to Last.fm API
    # For usage of the pylast package, type help(pylast) after importing
    password_hash = pylast.md5(api_data['password'])
    network = pylast.LastFMNetwork(
        api_key=api_data['key'],
        api_secret=api_data['shared_secret'],
        username=api_data['username'],
        password_hash=password_hash)

    # Get the information from lastfm servers
    try:
        tagObj = network.get_tag(lfmTag)
        recommendedAlbum = tagObj.get_top_albums()[0].item
        albumTTags = recommendedAlbum.get_top_tags(limit=250)

        # Make a vector from the album
        albumVec = get_album_vector(albumTTags, pikfile)
        return (str(recommendedAlbum), albumVec)

    except Exception as e:
        print("Something went wrong. Maybe the input arguments are incompatible. The error message is:")
        print(e)


def get_album_vector(albumTTags, pikfile):
    """
    Get the tags associated with an album
    Insert weights if they appear in our tag list
    """
    tag_list = open_all_tags(pikfile)

    albumList = []
    for tag in tag_list:
        done = False
        for topTag in albumTTags:
            tTagStr = str(topTag.item)
            if tTagStr == tag:
                albumList.append(int(topTag.weight))
                done = True
        if done is False:
            albumList.append(0)

    return np.array(albumList)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gets the topalbums from\
        a lastfm tag given in the input')
    parser.add_argument('lfmtag', help='tag to get the topalbums from')
    parser.add_argument('pikfile', help='path to sorted list of tags')
    args = parser.parse_args()
    # Path to the data for your API key. Since it requires your password we
    # should all have our own. The path shown here ('.api_key') is also in the
    # .gitignore, so I would advise you to duplicate this. A format for this
    # can be found in the README
    secretfile = '.api_key'
    with open(secretfile) as f:
        userdata = json.load(f)
        get_top_album(userdata, args.lfmtag, args.pikfile)

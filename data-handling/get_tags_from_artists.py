import pylast
import json
import argparse
import csv
import os


def write_to_file(fdict, filename):
    # filename is still with extension, change it to .json
    filename, ext = os.path.splitext(filename)
    with open(filename + ".json", "w") as outfile:
        json.dump(fdict, outfile, indent=2)


def main(api_data, user_file, ones=True):
    # Connect to Last.fm API
    # For usage of the pylast package, type help(pylast) after importing
    password_hash = pylast.md5(api_data['password'])
    network = pylast.LastFMNetwork(
        api_key=api_data['key'],
        api_secret=api_data['shared_secret'],
        username=api_data['username'],
        password_hash=password_hash)

    # Open up a tab separated user file to process
    with open(user_file, 'r') as datafile:
        tsvin = csv.reader(datafile, delimiter='\t')
        already_done = []
        writeback_dict = {}
        for dataline in tsvin:
            # dataline = [userid, artistid, artistname, trackid, trackname]
            try:
                # Find artist of track -> top tags of artist
                artist = pylast.Artist(dataline[3], network)
                # Skip artists we've already gotten the tags from
                if artist not in already_done:
                    already_done.append(artist)
                    # Get top tags
                    ts = artist.get_top_tags()
                    # Store and count tags
                    for tag in ts:
                        t = tag[0].name
                        if t in writeback_dict:
                            writeback_dict[t] += 1
                        else:
                            writeback_dict[t] = 1
            except Exception as e:
                continue

        # If specified, only keep values larger than 1
        if not ones:
            writeback_dict = {k: v for k, v in writeback_dict.items() if v > 1}
        write_to_file(writeback_dict, user_file)
        print("Done!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A data preprocessor for\
    the last-fm 1K dataset. Outputs the tags of albums that tracks belong to')
    parser.add_argument('data', help='data folder with songs titles (.tsv)')
    parser.add_argument('--no-ones', dest='ones', action='store_false',
                        help='Dont store tags with only one occurrence',
                        default=True)
    args = parser.parse_args()
    # Path to the data for your API key. Since it requires your password we
    # should all have our own. The path shown here ('.api_key') is also in the
    # .gitignore, so I would advise you to duplicate this. A format for this
    # can be found in the README
    secretfile = '.api_key'
    with open(secretfile) as f:
        userdata = json.load(f)
        main(userdata, args.data, args.ones)

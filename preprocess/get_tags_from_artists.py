import pylast
import json
import argparse
import csv
import os


def write_to_file(fdict, filename):
    # Save the give dict to a json file with a similar filename
    # filename is still with extension, change it to .json
    filename, ext = os.path.splitext(filename)
    with open(filename + ".json", "w") as outfile:
        json.dump(fdict, outfile, indent=2)


def main(api_data, user_file, ones=10):
    # Connect to Last.fm API
    # For usage of the pylast package, type help(pylast) after importing
    password_hash = pylast.md5(api_data['password'])
    network = pylast.LastFMNetwork(
        api_key=api_data['key'],
        api_secret=api_data['shared_secret'],
        username=api_data['username'],
        password_hash=password_hash)

    # Open up a tab separated file representing a user
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
                # Skip if we encouter an error
                continue

        # Only keep values larger than the specified number of occurrences
        writeback_dict = {k: v for k, v in writeback_dict.items() if v > ones}
        # Save the final dict
        write_to_file(writeback_dict, user_file)
        print("Done!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A data preprocessor for\
    the last-fm 1K dataset. For a tab separated file, looks up the tags for\
    each artist and puts it in a json file together with its count')
    parser.add_argument('data', help='data file with song titles (.tsv)')
    parser.add_argument('--limit', dest='ones', type=int, metavar='N',
                        help='Only store tags with more than N occurrences',
                        default=10)
    args = parser.parse_args()
    # Path to the data for your API key. Since it requires your password we
    # should all have our own. The path shown here ('.api_key') is also in the
    # .gitignore, so I would advise you to duplicate this. A format for this
    # can be found in the README
    secretfile = '.api_key'
    with open(secretfile) as f:
        userdata = json.load(f)
        main(userdata, args.data, args.ones)

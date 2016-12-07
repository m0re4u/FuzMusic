import pylast
import json
import argparse
import csv


def main(api_data, artist_file):
    password_hash = pylast.md5(api_data['password'])
    network = pylast.LastFMNetwork(
        api_key=api_data['key'],
        api_secret=api_data['shared_secret'],
        username=api_data['username'],
        password_hash=password_hash)
    # For usage of the pylast package, type help(pylast) after importing

    # Open up a txt file of artists to see how tag extraction works
    with open(artist_file, 'r') as datafile:
        tsvin = csv.reader(datafile, delimiter='\t')
        already_done = []
        for dataline in tsvin:
            try:
                # Find track -> album -> top tags
                nr = pylast.Track(dataline[3], dataline[5], network)
                album = nr.get_album()
                if album not in already_done:
                    ts = album.get_top_tags()
                    # writeback should be here
                    print([tag[0].name for tag in ts])
                    already_done.append(album)
            except Exception as e:
                print("Did not find: {} - {}".format(dataline[3], dataline[5]))
                continue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A data preprocessor for\
    the last-fm 1K dataset. Outputs the tags of albums that tracks belong tos')
    parser.add_argument('data', help='data folder with songs titles (.tsv)')
    args = parser.parse_args()
    # Path to the data for your API key. Since it requires your password we
    # should all have our own. The path shown here ('.api_key') is also in the
    # .gitignore, so I would advise you to duplicate this. A format for this
    # can be found in the README
    secretfile = '.api_key'
    with open(secretfile) as f:
        userdata = json.load(f)
        main(userdata, args.data)

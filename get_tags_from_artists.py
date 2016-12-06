import pylast
import json


def main(api_data, artist_file):
    password_hash = pylast.md5(userdata['password'])
    network = pylast.LastFMNetwork(
        api_key=userdata['key'],
        api_secret=userdata['shared_secret'],
        username=userdata['username'],
        password_hash=password_hash)
    # For usage of the pylast package, type help(pylast) after importing

    # Open up a txt file of artists to see how tag extraction works
    with open(artist_file) as fa:
        for artist in fa:
            # Remove newline characters
            artist = artist.strip('\n')
            try:
                lastfm_artist = network.get_artist(artist)
                artist_tags = lastfm_artist.get_top_tags()
                # Print tags for now, we'd probably want to store these
                print([tag[0].name for tag in artist_tags])
            # Handle the exception where the artist wasn't found
            except pylast.WSError:
                print("{} not found".format(artist))
                continue

if __name__ == '__main__':
    # Path to the data for your API key. Since it requires your password we
    # should all have our own. The path shown here ('.api_key') is also in the
    # .gitignore, so I would advise you to duplicate this
    secretfile = '.api_key'
    # This is a dummy file for now, every line containing one artist.
    # In the future, we can change this to our real data, where we have lines
    # of tracks from a certain artist. We can then either extract tags from
    # those tracks, or lookup the album the track was on and extract its tags.
    dummy_artists = 'artists.txt'
    with open(secretfile) as f:
        userdata = json.load(f)
        main(userdata, dummy_artists)

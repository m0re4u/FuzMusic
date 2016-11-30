import gzip
import pylast
import musicbrainzngs


def main(bigdatafile):
    with gzip.open(bigdatafile, 'rb') as f:
        for line in f:
            print(line.split(b'\t'))


if __name__ == '__main__':
    main("/home/m0re/data/lastfm-dataset-360K.tar.gz")

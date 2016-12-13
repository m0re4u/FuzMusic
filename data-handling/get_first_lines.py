import csv
import sys
import os
import argparse


def main(filename):
    """
    Will split the big input file of 1000 user into 1000 files of 1 user
    """
    with open(filename) as origfile:
        dir = os.path.dirname(filename)
        csv_reader = csv.reader(origfile, delimiter='\t')

        # Fixes a bug:
        # http://stackoverflow.com/questions/15063936/csv-error-field-larger-than-field-limit-131072
        csv.field_size_limit(sys.maxsize)
        lastuser = None
        for row in csv_reader:
            if lastuser != row[0]:
                print(row[0])
                lastuser = row[0]
            with open(os.path.join(dir, "split", lastuser + ".txt"), "a") as f:
                f.write("{}\n".format("\t".join(row)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A data preprocessor for\
    the last-fm 1K dataset. Will split the big input file of 1000 user into\
    1000 files of 1 user')
    parser.add_argument('data', help='data folder with songs titles (.tsv)')
    args = parser.parse_args()
    main(args.data)

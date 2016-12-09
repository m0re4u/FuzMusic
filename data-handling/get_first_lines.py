#!/usr/bin/env python3
import binascii
import csv
import os.path
import sys

def main(filename, newfile):
    with open(filename) as origfile:
        csv_reader = csv.reader(origfile, delimiter='\t')
        with open(newfile, mode='w') as csvfile:

            csvwriter = csv.writer(csvfile, delimiter = '\t')
            k = 1
            for row in csv_reader:
                if k < 100:
                    csvwriter.writerow(row)
                    k = k+1
                else:
                    break

if __name__ == '__main__':
    filename = sys.argv[1]
    newfile = sys.argv[2]
    main(filename, newfile)

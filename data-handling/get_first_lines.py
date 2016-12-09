import csv
import sys


def main(filename, newfile):
    """
    Will split the big input file of 1000 user into 1000 files of 1 user
    """
    with open(filename) as origfile:
        csv_reader = csv.reader(origfile, delimiter='\t')
        with open(newfile, mode='w') as csvfile:

            csvwriter = csv.writer(csvfile, delimiter='\t')
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

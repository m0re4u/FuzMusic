#!/usr/bin/env python3
import binascii
import csv
import os.path
import sys
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.simpledialog import askinteger

def split_csv_file(f, dst_dir, keyfunc):
     csv_reader = csv.reader(f,delimiter='\t')
     csv_writers = {}
     for row in csv_reader:
         k = keyfunc(row)
         if k not in csv_writers:
             csv_writers[k] = csv.writer(open(os.path.join(dst_dir, k),
                                              mode='w', newline=''))
         csv_writers[k].writerow(row)

def get_args_from_cli():
     input_filename = sys.argv[1]
     column = int(sys.argv[2])
     dst_dir = sys.argv[3]
     return (input_filename, column, dst_dir)

def get_args_from_gui():
     input_filename = askopenfilename(
         filetypes=(('TSV', '.tsv'),),
         title='Select TSV Input File')
     column = askinteger('Choose Table Column', 'Table column')
     dst_dir = askdirectory(title='Select Destination Directory')
     return (input_filename, column, dst_dir)

if __name__ == '__main__':
     if len(sys.argv) == 1:
         input_filename, column, dst_dir = get_args_from_gui()
     elif len(sys.argv) == 4:
         input_filename, column, dst_dir = get_args_from_cli()
     else:
         raise Exception("Invalid number of arguments")
     with open(input_filename, mode='r', newline='') as f:
         split_csv_file(f, dst_dir, lambda r: r[column-1]+'.tsv')

         #split_csv_file(f, dst_dir, lambda r: binascii.b2a_hex(r[column-1].encode('utf-8')).decode('utf-8')+'.tsv')

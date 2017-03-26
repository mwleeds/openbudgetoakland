"""
This script reads CSV files downloaded from open.ua.edu and deletes some of
the commas because the fields aren't quoted as they should be.
"""

import csv
import sys
from collections import Counter


def main():
    out = open('ua_finances_2016_fixed.csv', 'w')
    with open('ua_finances_2016.csv') as in_file:
        for i,line in enumerate(in_file):
            line = line.strip()
            line = line[1:]
            if len(line) == 0: continue
            if line[-1] == ',':
                line = line[:-1]
            comma_count = line.count(',')
            if i > 0 and comma_count > 10:
                old_line_fields = line.split(',')
                new_line_fields = [old_line_fields[0]] + [''.join(old_line_fields[1:(2 + comma_count - 10)])] + old_line_fields[(2 + comma_count - 10):]
                line = ','.join(new_line_fields)
            out.write(line + '\n')
    out = open('ua_finances_2015_fixed.csv', 'w')
    with open('ua_finances_2015.csv') as in_file:
        column_values = {}
        for i,line in enumerate(in_file):
            line = line.strip()
            if line[-2:] == ',,':
                line = line[:-2]
            if line[-1] == ',':
                line = line[:-1]
            comma_count = line.count(',')
            if comma_count > 10:
                old_line_fields = line.split(',')
                new_line_fields = [old_line_fields[0]] + [''.join(old_line_fields[1:(2 + comma_count - 10)])] + old_line_fields[(2 + comma_count - 10):]
                line = ','.join(new_line_fields)
            out.write(line + '\n')


if __name__=='__main__':
    main()

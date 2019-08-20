#!/usr/bin/env python 

import sys
import os
import re

file_path = os.getenv("map_input_file")
file_name = file_path.split('/')
file_name = file_name[-1]
year = re.search(r'\d+', file_name).group()
#UNITID, CIPCODE, GRAND TOTAL, YEAR -
#Link HDXXXX tables for institute details.
for line in sys.stdin:
	# UNITID - 0
	# cipcode - 1
	# GRADN TOTAL - 5
	indexes = [0, 1, 5]
	row = line.split(',')
	if row[0] == "UNITID":
		continue
	elif row[1] == "\"99\"":
		continue
	else:
		print('{0},{1},{2},{3}'.format(row[0], row[1].strip('\"'), row[5], year))

#year = re.search(r'd+', file_name[-1]).group()
#print('{0}, 1'.format(year))

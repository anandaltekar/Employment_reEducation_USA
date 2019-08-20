#!/usr/bin/env python 

import sys
import os
import re

file_path = os.getenv("map_input_file")
file_name = file_path.split('/')
file_name = file_name[-1]
year = re.search(r'\d+', file_name).group()
#Top Courses from each university -
#Link HDXXXX tables for institute details.
for line in sys.stdin:
	# cipcode1 - 2
	# cipcode2 - 39
	# cipcode3 - 45
	# cipcode4 - 51
	indexes = [0, 2, 39, 45, 51]
	row = line.split(',')
	if row[0] == "UNITID":
		continue
	else:
		print('{0},{1},{2},{3},{4},{5}'.format(row[0], row[2], row[39], row[45], row[51], year))

#year = re.search(r'd+', file_name[-1]).group()
#print('{0}, 1'.format(year))

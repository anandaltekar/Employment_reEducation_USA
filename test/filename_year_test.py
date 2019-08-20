#!/usr/bin/env python 

from __future__ import print_function
import sys
import os
import re

#Using System Variables to get the name of the input file, which contain the year of the data
file_path = os.getenv("map_input_file")
file_name = file_path.split('/')
file_name = file_name[-1]
year = re.search(r'\d+', file_name).group()

for line in sys.stdin:
	line = line.split(',')
	print(year)

#year = re.search(r'd+', file_name[-1]).group()
#print('{0}, 1'.format(year))

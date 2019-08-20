#!/usr/bin/env python 

import sys
import os
import re

#UNITID, INSTNM, STABBR -
#FROM HDXXXX.
for line in sys.stdin:
	# UNITID - 0
	# INSTNM - 1
	# STABBR - 5
	indexes = [0, 1, 5]
	row = line.split(',')
	if row[0] == "UNITID":
		continue
	else:
		print('{0},{1},{2}'.format(row[0], row[1].strip('\"'), row[5].strip('\"')))

#year = re.search(r'd+', file_name[-1]).group()
#print('{0}, 1'.format(year))

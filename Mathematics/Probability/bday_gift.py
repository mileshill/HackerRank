#!/usr/bin/python python

import numpy as np
from sys import stdin
from collections import defaultdict


# reader
r = stdin.readline

# Number of elements
N = int( r() )

# Read in all elements
x = np.zeros( N ,dtype=np.int32)
p = defaultdict(int)

for elem in range(N):
	num = r().strip()
	x[ elem ] = int( num )
	p[ num ] += 1.0/N 

ex = 0.0
for elem in x:
	ex += elem * p[ str(int(elem))]

print( "{0:.1f}".format(ex) )


y = np.bincount(x)
ii = np.nonzero(y)[0]

print( np.dot( ii, y[ii] ))

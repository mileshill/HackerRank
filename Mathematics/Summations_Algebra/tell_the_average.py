#!/usr/bin/evn python

from sys import stdin
import numpy as np
from functools import reduce

r = stdin.readline

length = int( r() )

all_nums = np.asarray( r().strip().split(), dtype=np.int32 )

element = reduce(lambda x,y: x + y + (x * y), all_nums)

avg = element / (length - 1)

print( avg )

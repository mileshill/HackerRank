from sys import stdin
from math import modf
r = stdin.readline

for line in range( int( r() ) ):
	n, m = map(float ,r().strip().split())
	frac_part, int_part = modf(n/m)
	
	if n < m:
		out = n *(n+1) / 2
	else:
		k = (m-1)*m / 2 
	
		out = int( (k*int_part + k*frac_part))

	print(int( out ))



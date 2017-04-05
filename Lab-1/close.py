#!/usr/bin/env python

import math

def close (a,b,c):
	if math.fabs(a-b) < c:
		return True
	else:
		return False

if __name__ == '__main__':
	print close (1,2,3)

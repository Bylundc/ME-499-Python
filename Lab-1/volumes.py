#!/usr/bin/env python

import math

#r is radius
#h is height
def cylinder_volume (r,h):
	if h < 0 or r < 0:
		return None
	else: 
		return h*r**2*math.pi

#R is major radius
#r is minor radius
def torus_volume (R,r):
	if R < 0 or r < 0:
		return None
	else:
		return (math.pi*r**2)*(2*math.pi*R)
	
	
if __name__ == '__main__':
	print cylinder_volume(3,5)
	print torus_volume(4,3)

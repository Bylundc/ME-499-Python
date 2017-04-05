#!/usr/bin/env python


import math
from complex import Complex

def roots (a,b,c): # ax^2 + bx + c = 0
	storage = ('roots:',) #create a tuple to store all my root findings
	d = (b**2)-(4*a*c)
	if d < 0:
		d_n = math.sqrt(abs(d))
		d_c = Complex(0, -d_n)
		sol1 = (-b + d_c)/(2*a)
		sol2 =(-b + (-1 *d_c))/(2*a)
		storage = storage + ('2 imaginary solutions 1: {0} , 2: {1}'.format(sol1, sol2),)
		return storage
	if d > 0:
		sol1 = (-b + math.sqrt(d))/(2*a)
		sol2 =(-b - math.sqrt(d))/(2*a)
		storage = storage + ('2 real solutions 1: {0} , 2: {1}'.format(sol1, sol2),)
		return storage
	if d == 0:
		sol1 = (-b + math.sqrt(d))/(2*a)
		sol2 =(-b - math.sqrt(d))/(2*a)
		storage = storage + ('1 real solution {0}'.format(sol1),)
		return storage

print roots(1,-3,4)
print roots(-4,12,-9)
print roots(2,-11,5)

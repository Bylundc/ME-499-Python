#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
"""
add more raw_inputs for corners of box and for sample size
"""
def area(f=0, p1 = (-3,-3), p2 = (3,3), samples=1000):
	# ask user for circle function parameters
	while True:
		try:
			a,b,r = raw_input("What are the coefficients to the circle function you would like to use? ax^2 + bx^2 - r^2 = 0\na,b,r: ").split(",")
			a = float(a)
			b = float(b)
			r = float(r)
		except ValueError:
			print "Incorrect input!\nTry again with numbers..."
			continue
		if a == 0 or b == 0 or r == 0:
			print "Incorrect input!\nCoefficients can't be zero..."
			continue
		else:
			break
	
	# print value of chosen function and sample size
	ranx =  list(np.random.uniform(p1[0],p2[0],size=samples))
	rany =  list(np.random.uniform(p1[1],p2[1],size=samples))
	inside = 0.0
	for i in xrange(samples):
		if a*ranx[i]**2 + b*rany[i]**2 - r**2 <= 0:
			inside += 1
	area = (inside/samples)*((p2[0]-p1[0])*(p2[1]-p1[1]))
	act_area = np.pi * r**2
	print area
	
	# print absolute error as list size increases
	err_area = []
	test_sample = xrange(1,1000)
	for k in xrange(len(test_sample)):
		inside = 0.0
		ranx =  list(np.random.uniform(p1[0],p2[0],size=test_sample[k]))
		rany =  list(np.random.uniform(p1[1],p2[1],size=test_sample[k]))
		for i in xrange(test_sample[k]):
			if a*ranx[i]**2 + b*rany[i]**2 - r**2 < 0:
				inside += 1
		area = (inside/test_sample[k])*((p2[0]-p1[0])*(p2[1]-p1[1]))
		err_area.append(abs(area - act_area))

	plt.title("Absolute Error of Actual - Estimate")
	plt.plot(test_sample,err_area,'r')
	plt.xlabel("Step Size")
	plt.ylabel("Error Value")
	plt.show()

if __name__ == "__main__":
	a = area(0,(-3,-3),(3,3))

#!/usr/bin/env python

import matplotlib.pyplot as pplot
from numpy import linspace

def integrate(f=[0,0,0],a=0,b=0,step=1):
	print "This integral approximation uses a right hand Riemann sum."
	# ask for function to integrate
	while True:
		try:
			x1,x2,x3 = raw_input("What are the coefficients to the quadriatic function you would like to integrate? ax^2 + bx + c\na,b,c: ").split(",")
			x1 = float(x1)
			x2 = float(x2)
			x3 = float(x3)
		except ValueError:
			print "Incorrect input!\nTry again with numbers..."
			continue
		if x1 == 0 and x2 == 0 and x3 == 0:
			print "Incorrect input!\nCoefficients can't all be zero..."
			continue
		else:
			break

	# ask for interval to integrate on
	while True:
		try: 
			a , b = raw_input("On what interval to approximate? a,b: ").split(",")
			a = float(a)
			b = float(b)
		except ValueError:
			print "Incorrect input!\nTry again with numbers..."
			continue
		if a > b:
			print "Incorrect input!\na is larger than b..."
			continue
		else:
			break

	# ask for step size
	while True:
		change = raw_input("Would you like to change the step size, default = 1? Y or N: ")
		if change.lower() in ["y", "yes"]:
			while True:
				try:
					step = float(raw_input("What is the step size? "))
				except ValueError:
					print "Incorrect Input!\nTry again with a number..."
					continue				
				if step < 0:
					print "Incorrect input!\nCan't be a negative number..."
					continue
				if step == 0:
					print "Incorrect input!\nCan't be zero..."
					continue
				else:
					break
			break
		elif change.lower() in ["n", "no"]:
			step = step
			break
		else:
			print "Incorrect input!\nType yes or no..."
			continue
	n = int(abs(b-a) / step)
	dx = step

	# use right riemann sum
	area = 0
	k = 0
	x = 0
	while x < b: 
		k += 1
		x = a + k * dx
		area += x1*x**2 + x2*x + x3
	
	area = dx * area
	print "Integral approximation of {0}x^2 + {1}x + {2} from {3} to {4} with {5} rectangles is: {6}".format(x1,x2,x3,a,b,n,area)
	
	#FOR PLOTTING ERROR!
	actual = ((x1*b**3)/3 + (x2*b**2)/2 + x3*b) - ((x1*a**3)/3 + (x2*a**2)/2 + x3*a)
	step = linspace(5,1e-5,100)
	dx = step[:]
	area_plt = []
	for i in xrange(len(dx)):
		area = 0
		k = 0
		x = 0
		while x < b: 
			k += 1
			x = a + k * dx[i]
			area += x1*x**2 + x2*x + x3
		area_plt.append(abs(area*dx[i]-actual))
	
	# Plot absolute error of function that was inputted
	pplot.title('Absolute Error of Actual - Estimate')
	pplot.plot(step,area_plt,'r')
	#pplot.ylim(area_plt[len(area_plt)-1]*0.9,area_plt[0]*1.1)
	pplot.xlabel('Step Size')
	pplot.ylabel('Error Value')
	pplot.grid()
	pplot.show()
	return ""

if __name__ == "__main__":
	print integrate()


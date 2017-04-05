#!/usr/bin/env python

import numpy as np

# circle class
class Circle:
	def __init__(self, radius):
		self.radius = radius

	def __str__(self):
		return 'Circle({0})'.format(self.radius)

	def area(self):
		return np.pi*(self.radius ** 2)

	def diameter(self):
		return 2 * self.radius

	def circumference(self):
		return 2 * np.pi * self.radius

if __name__ == '__main__':     
	shape = [Circle(3)]

	for s in shape:
		print s         
		print '  area:', s.area()         
		print '  perimeter:', s.diameter()
		print '  circumference:', s.circumference()


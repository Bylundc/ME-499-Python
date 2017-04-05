#!/usr/bin/env python

import numpy as np

class Complex:
	def __init__(self, re = 0, im = 0):
		self.re = re #real
		self.im = im #imaginary

	def __str__(self):
		if self.im >= 0:
			return '({0} + {1}i)'.format(self.re, self.im)
		if self.im < 0:
			return '({0} - {1}i)'.format(self.re, abs(self.im))
		if self.re == 0:
			return '({0} + {1}i)'.format(self.re, self.im)
# ADDITION
	def __add__(self, other):
		if isinstance(other, (float,int)):
			return Complex(self.re + other, self.im)
		else:
			return Complex(self.re + other.re, self.im + other.im)
	def __radd__(self, other):
		return self + other

# SUBTRACTION
	def __sub__(self, other):
		if isinstance(other, (float,int)):
			return Complex(other - self.re, self.im)
		else:
			return Complex(self.re - other.re, self.im - other.im)
	def __rsub__(self, other):
		return self - other

# MULTIPLICATION
	def __mul__(self, other):
		if isinstance(other, (float,int)):
			return Complex(self.re * other, self.im * other)
		else:
			return Complex(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)
	def __rmul__(self, other):
		return self * other

# DIVISION
	def __div__(self, other):
		if isinstance(other, (float,int)):
			x = float(other**2)
			y = self * Complex(other)
			re = y.re / x
			im = y.im / x
			return Complex(re , im)
		else:
			x = float(other.re**2 + other.im**2)
			y = self * Complex(other.re, - other.im)
			re = y.re / x
			im = y.im / x
			return Complex(re , im)
	def __rdiv__(self, other):
		return self / other

# COMPLEX CONJUGATE
	def __invert__(self):
		if self.im >= 0:
			return '({0} - {1}i)'.format(self.re, abs(self.im))
		if self.im < 0:
			return '({0} + {1}i)'.format(self.re, abs(self.im))

	__repr__=__str__


if __name__ == '__main__':
	# Test for ALL types of complex numebers
	a = Complex(1.0, 2.3)
	b = Complex(2)
	c = Complex()
	d = Complex(0, 2)
	e = Complex(0, -2)
	f = Complex(-2, -3)

	print 'Complex General Test'
	print a
	print b
	print c
	print d
	print e
	print f
	
	
	# Test for addition
	a = Complex(1, 2)
	b = Complex(3, 4)
	
	print 'Addition Test'
	print a + b
	print a + 1
	print 1 + a
	

	# Test for subtraction
	a = Complex(1, 2)
	b = Complex(3, 4)
	
	print 'Subtraction Test'
	print a - b
	print b - 1
	print 1 - b

	# Test for multiplication
	a = Complex(1, 2)
	b = Complex(3, 4)
	
	print 'Multiplication Test'
	print a * b
	print 2 * a
	print b * 3

# Test for division
	a = Complex(1, 2)
	b = Complex(3, 4)
	
	print 'Division Test'
	print a / b
	print a / 2
	print b / 3
	
# Test comple conjugate
	a = Complex(1, 2)
	b = Complex(3, -4)
	
	print 'Conjugate Test'
	print ~a
	print ~b

#!/usr/bin/env python

#The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder. One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, then gcd (a,b) = gcd(b,r). As a base case, we can use gcd(a,0) = a. Write a function called gcd that takes parameters a and b and returns their greatest common divisor.

# Set some variables to use
a = 12
b = 24

def gcd (a,b):
	if a > b:
		smaller = b
	else:
		smaller = a
	for i in range(1,smaller+1,1):
		if((a % i == 0) and (b % i == 0)):
			GCD = i
	return GCD

# Check code for errors among known gcd values
if __name__ == '__main__':
	if gcd(12,24) != 12:
		print ('Break')
	if gcd(48,30) != 6:
		print ('Break')
	print ('All Tests Done')

	print (gcd(a, b))

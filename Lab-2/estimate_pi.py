#!/usr/bin/env python

import math

# for the factorial portion
def factorial(n):
	if n == 0:
		return 1	
	else:
	  fact = 1
	  for i in range(1,n + 1):
		fact = fact * i 
	  return fact

# for the series portion
def series_term(k):
	num = factorial(4*k) * (1103 + 26390*k)
	den = factorial(k)**4 * 396**(4*k)
	return float (num) / (den)

def estimate_pi():
	k = 0
	final = 0
	while True:
		term = series_term(k)
		final += term
		if term < 1e-15:
			break
		else:
			k += 1
	f = 2 * math.sqrt(2) / 9801
	est = 1 / (final * f)
	return est

# check code for errors
if __name__ == '__main__':
# check for errors in factorial function
	if factorial(0) != 1:
		print ('Factorial function broken for 0!')
	if factorial(1) != 1:
		print ('Factorial function broken for 1!')
	if factorial(7) != 5040:
		print ('Factorial function broken for all values!')
# check for errors in pi estimate
	if estimate_pi() != math.pi:
		print('Pi estimation is wrong')
	print ('All Tests Done')
# print estimated pi value
	print estimate_pi()

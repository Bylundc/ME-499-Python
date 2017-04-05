#!/usr/bin/env python

# lists to be used
numbersi = [1,2,3,4,5]
numbersr = [3,3,2]

# iterative sum function
def sum_i (ni):
	total = 0
	for i in ni:
		total += i
	return total

# recursive sum function
def sum_r (nr):
	f = 0
	if len(nr) == 0:
		return [0]
	elif len(nr) == 1:
		return nr[0]
	else:
		return nr[0] + sum_r(nr[1:])

# Test section
if __name__ == '__main__':
	if sum_i(numbersi) != sum(numbersi):
		print 'Wrong iterative'
	if sum_r(numbersr) != sum(numbersr):
		print 'Wrong recursive'
	print 'All Tests Done'
	print 'Iterative sum:',numbersi,'=',(sum_i(numbersi))	
	print 'Recursive sum:',numbersr,'=',(sum_r(numbersr))

#!/usr/bin/env python

# list to be used
listi = ['blah','hello','wrong','window','test','length','jeep']
listr = [1,2,3,4,5]



# iterative reverse function
def reverse_i (l):
	listb = l[:]
	if len(l) == 0:
		return l
	elif len(l) == 1:
		return l
	else:
		for i in range(len(listi)):
			listi[i] = listb[-(i+1)]
		return listi

# recursive reverse function
def reverse_r (l):
	if len(l) == 0:
		return l
	elif len(l) == 1:
		return l
	else:
		return [l[-1]] + reverse_r(l[:-1])

# Test section

list_ti = listi[:] # To test iterative list
list_ti.reverse()

list_tr = listr[:] # To test recursive list
list_tr.reverse()

if __name__ == '__main__':
	
	# for iterative
	if reverse_i(listi) != list_ti:
		print 'Iterative reverse broken'
	if reverse_i([]) != []:
		print 'Iterative reverse broken'
	if reverse_i(['hello']) != ['hello']:
		print 'Iterative reverse broken'
	
	# for recursive
	if reverse_r(listr) != list_tr:
		print 'Recursive reverse broken'
	if reverse_r([]) != []:
		print 'Recursive reverse broken'
	if reverse_r(['hello']) != ['hello']:
		print 'Recursive reverse broken'
	print 'All Tests Done'
	
	# Print reversed lists
	print 'Iterative reverse'
	print 'Original:',(listi)
	print 'New list:',(reverse_i(listi))

	print 'Recursive reverse'
	print 'Original:',(listr)
	print 'New list:',(reverse_r(listr))	

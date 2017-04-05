#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import timeit

# use bubblesort function adapted from my brain and the internet...
def bubblesort (lst):
	william = lst[:] # use william as the name of the copied list
	if len(william) > 1:
		for k in xrange(len(william)-1,0,-1):
			for i in xrange(k):
				if william[i] > william [i+1]:
					srtd = william[i]
					william[i] = william[i+1]
					william[i+1] = srtd
		return william
	else:
		return lst

# create me a quick sort algorithm utilizing my google skills and knowledge of lists
def quicksort (lst):
    less = []
    equal = []
    greater = []
    
    billy = lst[:] # use billy as the name of the copied list
    if len(billy) > 1:
        pivot = billy[np.random.randint(0,len(billy),size=1)]
        for i in billy:
            if i < pivot:
                less.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                greater.append(i)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return lst

### TESTING FUNCTION for bubblesort and quicksort return True if list IS sorted
def is_sorted (lst):	
	bsort = bubblesort(lst)
	qsort = quicksort(lst)
	if all(bsort[i] <= bsort[i+1] for i in xrange(len(bsort)-1)) and all(qsort[i] <= qsort[i+1] for i in xrange(len(qsort)-1)):
		return True
	else:
		return False

# if testing function is True then run while loop below
test = list(np.random.randint(0,1000,size=10))

## For Part ONE
total_time = []
ttime = []
k = 1
if is_sorted(test) == True:
	while True:
		lstn = list(np.random.randint(0,1000,size=2e3))
		if k <= 10:
			start = timeit.time.time()
			bubblesort(lstn)
			end = timeit.time.time()
			total_time += [float(end - start)]
			
			strt = timeit.time.time()
			quicksort(lstn)
			nd = timeit.time.time()
			ttime += [float(nd - strt)]

			k += 1
		else:
			break
#	For bubblesort
	avg_time = sum(total_time)/len(total_time)
	print 'Average bubblesort time of 10 samples:',avg_time
#	For quicksort
	avtime = sum(ttime)/len(ttime)
	print 'Average quicksort time of 10 samples :',avtime

else:
	print 'Something went wrong'

## For Part FOUR

# make a list from 0 to 2000 counting by 100's
values = list(np.arange(0,2100,100))

if is_sorted(test) == True:
	ttime = []
	for i in values:
		lstn = list(np.random.randint(0,1000,size=i))

		strt = timeit.time.time()
		quicksort(lstn)
		nd = timeit.time.time()
		ttime += [float(nd - strt)]

	plt.title('Time to Run Quicksort')
	plt.plot(values,ttime,'r')
	plt.xlabel('List Length')
	plt.ylabel('Time in sec')
	plt.grid()
	plt.show()
else:
	print 'Something went wrong'



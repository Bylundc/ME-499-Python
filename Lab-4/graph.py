#!/usr/bin/env python

import matplotlib.pyplot as plt
import timeit
import numpy as np

# use bubblesort function adapted from my brain and the internet...
def bubblesort (lst):
	william = lst[:] # use william as the name of the list copy
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

# make a list from 0 to 2000 counting by 100's
values = list(np.arange(0,2100,100))

total_time = []
totaltime = []
for i in values:
		lstn = list(np.random.randint(0,1000,size=i))

		start = timeit.time.time()
		bubblesort(lstn)
		end = timeit.time.time()
		total_time += [float(end - start)]

		strt = timeit.time.time()
		sorted(lstn)
		nd = timeit.time.time()
		totaltime += [float(nd - strt)]

print total_time

plt.subplot(211)
plt.title('Time to Run Bubblesort vs Sorted')
plt.plot(values,total_time,'b', label='bubblesort')
plt.xlabel('List Length')
plt.ylabel('Time in sec')
plt.legend()
plt.grid()

plt.subplot(212)
plt.plot(values,totaltime,'r', label='sorted')
plt.xlabel('List Length')
plt.ylabel('Time in sec')
plt.legend()
plt.grid()

plt.show()



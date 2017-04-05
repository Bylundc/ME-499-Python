#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import timeit

# list lengths to be used
values = [1,10,100,1000,10000,100000,1000000]

# create random values
def ransor(k):
	return list(np.random.randint(0,1000,size=k))

# function for sorted and sum
def tsort(k):
	return sorted(ransor(k))
def sumer(k):
	return sum(ransor(k))


# time for sorted
k = 1
total_time = []
while True:
	if k <= 1e6:
		start = timeit.time.time()
		tsort(k)
		end = timeit.time.time()
		total_time += [float(end - start)]
		k = 10*k
	else:
		break

for i in total_time:
	print 'Time for sorted'
	print 'seconds: ', i

# time for sum
z = 1
total_times = []
while True:
	if z <= 1e6:
		starts = timeit.time.time()
		sumer(z)
		ends = timeit.time.time()
		total_times += [float(ends - starts)]
		z = 10*z
	else:
		break
for d in total_times:
	print 'Time for sum'
	print 'seconds: ', d

# plot the time of the two functions
plt.plot(values,total_time,'r', label='sorted')
plt.plot(values,total_times,'b', label='sum')
plt.title('Time to sort or sum a random list')
plt.xlabel('List length')
plt.ylabel('Time (sec)')
plt.legend()



plt.show()

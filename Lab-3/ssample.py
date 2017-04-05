#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

lists = []
k = 0

# sum 10 random numbers that are 0 to 1 and continually add that to a list called lists
while True:
	if k < 10000:
		lists.append(sum(np.random.random_sample(10))) 
		k += 1
	else:
		break

# plot the occurances of each sum on a histogram 
n, bins, patches = plt.hist(lists, 30, facecolor='r')
plt.title('Histogram')
plt.xlabel('Sum of 10 random numbers')
plt.ylabel('Occurances')
plt.show()

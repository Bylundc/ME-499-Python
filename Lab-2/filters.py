#!/usr/bin/env python

#import Gnuplot, Gnuplot.funcutils
import numpy
from sensor import *

# load raw data in
rawme = numpy.loadtxt("raw",usecols=(1,))
print rawme
# load raw data in
rawmed = numpy.loadtxt("raw",usecols=(1,)) 

# define a MEAN filter
def filtme(data):
	k = 0
	filtered = []
	while True:	
		filtered += [sum(data[k:k+w])/w]
		if k < len(data)-w:
			k +=1
		else:
			break
	return filtered

# define a MEDIAN filter
def filtmed(data, w = 3):
	k = 0
	filteredm = []
	while True:	
		filteredm += [numpy.median(rawmed[k:k+w])]
		if k < len(rawmed)-w:
			k +=1
		else:
			break
	return filteredm

# Ask for a filter width
w = int(raw_input('Enter a filter width: ')) #width
if w % 2 == 0:
	print "Width is even, choose an odd number."
elif w < 0:
	print "Width is negative, choose a positive number."
else:
	print filtme(rawme)

	"""
	# save filtered data
	print_sensor_data(filtme(rawme), 'filtered')
	# load in filtered data
	filtered = numpy.loadtxt("filtered",usecols=(1,))
	# plot raw data vs filtered data - MEAN
	gplot = Gnuplot.Gnuplot(persist=1)
	gplot.title("Filtered Data vs Raw - Mean")
	rawme = Gnuplot.PlotItems.Data(rawme, with_="linespoints lt rgb 'blue' lw 1 pt 1", title="raw")
	filteredme = Gnuplot.PlotItems.Data(filtered, with_="linespoints lt rgb 'black' lw 1 pt 1", title="filtered")
	gplot.plot(rawme,filteredme)
	
	# save filtered data
	print_sensor_data(filtmed(rawmed), 'filteredm')
	# load in filtered data
	filteredm = numpy.loadtxt("filteredm",usecols=(1,))
	# plot raw data vs filtered data - MEDIAN
	g = Gnuplot.Gnuplot(persist=1)
	g.title("Filtered Data vs Raw - Median")
	rawmed = Gnuplot.PlotItems.Data(rawmed, with_="linespoints lt rgb 'blue' lw 1 pt 1", title="raw")
	filteredmed = Gnuplot.PlotItems.Data(filteredm, with_="linespoints lt rgb 'red' lw 1 pt 1", title="filtered")
	g.plot(rawmed,filteredmed)
	"""

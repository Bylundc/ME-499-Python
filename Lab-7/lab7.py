#!/usr/bin/env python

from grabber import Webcam
import time
import matplotlib.pyplot as plt
import numpy as np

class Intensity:
	#Define the url to use, the MU webcam, Use a try block in order to remove the URL reject
	def __init__(self, url='http://mu.webcam.oregonstate.edu/'):
		self.MU = Webcam(url)
		while True:
			try:
				self.grabbed = self.MU.grab_image_data() #create a value with image data to use later
				break
			except:
				continue

	# Grab some data over x amount of time
	def collect_data(self):
		x = 1 # amount of time in minutes
		self.raw_average = []
		self.elapsed_time = []
		start = float(time.time()) # start the timer

		# Take the image and for each pixel save the r,g,b intesity values as a tuple in a list. Values range from 0,255.
		while True:	
			try:	# have to call this in order to continually grab images, again in a try block
				pixel_tuple = self.MU.grab_image_data() 
			except:
				continue
			average = []
			k = 0
			for pixel in xrange(len(pixel_tuple)):	#Save all the image data in a list called average
				average.append(float((pixel_tuple[pixel][k]+pixel_tuple[pixel][k+1]+pixel_tuple[pixel][k+2])/3))
			self.raw_average.append(float(sum(average) / len(average))) #Save the overall average in raw_average
	
			now = float(time.time()) #take the current time
			self.elapsed_time.append(now - start) #calculate the time since the script started
			time.sleep(1) #delay for 1 second
			if self.elapsed_time[len(self.elapsed_time)-1] > 60*x: #run this code for x minutes total
				break

	# Do something to filter the data, use a MEAN filter
		w = 7 #filter width to be used
		k = 0
		self.filtered_average = []
		self.filtered_time = []
		while True:	
			self.filtered_average.append(sum(self.raw_average[k:k+w])/w) # filter the previous average values
			self.filtered_time.append(sum(self.elapsed_time[k:k+w])/w) # filter the previous elapsed time
			if k < len(self.raw_average)-w:
				k +=1
			else:
				break
		
		return self.elapsed_time, self.raw_average, self.filtered_time, self.filtered_average
	
	# use this to plot the unfiltered and filtered data
	def plot_data(self):
		try: # check to see if there is any data that exists.
			# Plot unfiltered
			plt.figure(1)
			plt.title("Average Light Intensity - Unfiltered")
			plt.plot(self.elapsed_time,self.raw_average,"r")
			plt.xlabel("Time, in seconds")
			plt.ylabel("Light Intensity")
			plt.grid()
			plt.savefig("unfiltered.png") # save this figure as a png

			# Plot Filtered
			plt.figure(2)
			plt.title("Average Light Intensity - Filtered")
			plt.plot(self.filtered_time,self.filtered_average,"b")
			plt.xlabel("Time, in seconds")
			plt.ylabel("Light Intensity")
			plt.grid()
			plt.savefig("filtered.png") # save this figure as a png

			plt.show()
		except:
			print "No data to be plotted, please collect some data using the collect_data function." #error message
	
	# determine if it is currently daytime or nighttime
	def daytime(self):
		
		while True:
			average = []
			k = 0
			for pixel in xrange(len(self.grabbed)): # grab an image and calculate the average pixel value
				average.append(float((self.grabbed[pixel][k]+self.grabbed[pixel][k+1]+self.grabbed[pixel][k+2])/3))
			is_it_daytime = (float(sum(average) / len(average)))

			if is_it_daytime >= 70: # check to see if the average is above 70, return True if so and False otherwise
				return True
			else:
				return False
	
	# determine the most reoccuring color
	def most_common_color(self):
		dic = {}
		propdic = {}
		proplist = []

		for rgb in self.grabbed: #DO NOT REMOVE BLACK BAR... 1024 x 24 = 24576 removes black bar above in order not to skew results.
			dic.setdefault(rgb, 0)
			dic[rgb] += 1

		# find the most recoccuring rgb tuple and determine what color this is.
		top_color = dic.get(max(dic, key = dic.get)),max(dic, key = dic.get)

		if top_color[1][0] > top_color[1][1] and top_color[1][0] > top_color[1][2]:
			color = "red"
		elif top_color[1][1] > top_color[1][0] and top_color[1][1] > top_color[1][2]:
			color = "green"
		elif top_color[1][2] > top_color[1][0] and top_color[1][2] > top_color[1][1]:
			color = "blue"
		elif top_color[1][0] > 175 and top_color[1][1] > 175 and top_color[1][2] > 175:
			color = "white"
		elif top_color[1][0] < 20 and top_color[1][1] < 20 and top_color[1][2] < 20:
			color = "black"
		else:
			color = "grey"

		# determine how often each color occurs
		for items in dic:
			if items[0] > items[1] and items[0] > items[2]:
				proplist.append("red")
			elif items[1] > items[0] and items[1] > items[2]:
				proplist.append("green") 
			elif items[2] > items[0] and items[2] > items[1]:
				proplist.append("blue")
			elif items[0] > 175 and items[1] > 175 and items[2] > 175:
				proplist.append("white")
			elif items[0] < 20 and items[1] < 20 and items[2] < 20:
				proplist.append("black")
			else:
				proplist.append("grey")
		for colors in proplist:
			propdic.setdefault(colors, 0)
			propdic[colors] += 1

		# determine the proportion that this one color occurs in the image
		proportion_of_color = round(float(propdic.get(color)) / len(proplist),4)

		#What color is this? What proportion of pixels have this color? (Answer these questions in a file called answers.txt)
		try:
			text_file = open("answers.txt", "w")
			text_file.write("The highest reoccuring RGB tuple is {0} and it appears {1} times.\nThe color of this tuple is mostly {2}.\nThis color occurs in {3}% of the image.".format(top_color[1],top_color[0],color,proportion_of_color*100))
			return "Answers saved to answers.txt"
		except:
			return "Answers could not be saved."

	# determine if there is motion in the image
	def motion(self):
		first_image = self.MU.grab_image_data() #grab an image
		time.sleep(2) #wait for 2 seconds
		second_image = self.MU.grab_image_data() #grab a second image
		
		# find the average euclidean distance in the image ie. sqrt((p1 - q1)^2 + (p2 - q2)^2)
		i = 0
		distance = []
		while i != len(first_image):
			distance.append(np.sqrt((first_image[i][0] - second_image[i][0])**2 + (first_image[i][1] - second_image[i][1])**2 + (first_image[i][2] - second_image[i][2])**2))
			i += 1
		average_distance = float(sum(distance)/len(distance))
		# Return True if distance is detected, False otherwise.		
		if Intensity().daytime() == True: #use one value during the day, and another at night
			if average_distance >= 6: # use 6 to filter out noise in the camera during the day
				return True
			else:
				return False
		else:
			if average_distance >= 13: # use 13 to filter out noise in the camera during the night
				return True
			else:
				return False

if __name__ == "__main__":
	a = Intensity()
	#a.collect_data()
	#a.plot_data()
	#print a.daytime()
	#print a.most_common_color()
	#print a.motion()




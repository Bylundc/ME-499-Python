#!/usr/bin/env python

import re

class Book:
	def __init__(self, filename):
	# read in a text file
		with open(filename, 'r') as f:
			self.lst = f.read().split()

	## remove duplicate words, symbols that aren't letters or numbers and make everything lowercase
		self.remove = re.sub(r'[^a-zA-Z0-9 ]', ' ', str(self.lst)).lower().split()
		
		self.fixed = set(self.remove)	
		
		self.let = []
		for l in self.remove:
			self.let += list(l)

	# find the number of words in the txt file
	def number_of_words(self):
		return len(self.lst)

	## what words are in one text file but not the other file
	def __sub__(self, otherfile):
		notin = []
		for word in self.fixed:
			if word not in otherfile.fixed:
				notin.append(word)
		return notin

	# find common words in a text file
	def common_words(self, n = 'yes'):
		dic = {}
		x = []		
		for word in self.remove:
			dic.setdefault(word, 0)
			dic[word] += 1

		prompt = raw_input('Yes to list all word occcurances or no to list a specific value: ')
		if prompt.lower() in ['n', 'no']:
			n = int(raw_input('What number of occurances to look for? '))
			for w in dic:
				if n == dic.get(w):
					x += [(dic.get(w),w)]
			return x
		elif prompt.lower() in ['y', 'yes']:
			print('Hold on while the list is sorted')
			for w in dic:
				x.append((dic.get(w),w))
			x.sort()
			return x
		else:
			return 'Incorrect input!'

	def print_letter_frequencies(self):
		ldic = {}
		x = []
		
		for letter in self.let:
			ldic.setdefault(letter, 0)
			ldic[letter] += 1
		
		for letter in ldic:
			x.append((letter,ldic.get(letter)))
		x.sort()
		return x

if __name__ == '__main__':
	a = Book('dictionary.txt')
	b = Book('war_and_peace.txt')
	#print a.number_of_words()
	#print b.number_of_words()
	#print b - a
	print b.common_words()
	#print b.print_letter_frequencies()


#!/usr/bin/env python

def letter_count(word, letter):
	count = 0
	word = word.lower()
	letter = letter.lower()
	for char in word:
		if letter == char:
			count += 1
	return count


print letter_count ('halLway','L')


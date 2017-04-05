#!/usr/bin/env python

import random

class MyPlayer:
	def __init__(self, name="bylundc"):
		self.name = name
		self.move = 1 # always start with paper
		self.dic = {} #create a dictionary that will store all previous moves

	def play(self, name):
		return self.move

	def learn(self, name, move):
		self.dic.setdefault(move,0) # save the values that the opponent plays
		self.dic[move] += 1

		# if we tie play what beats the tie
		if self.move == move: 
			if self.move == 0:
				self.move = 1				
			elif self.move == 1:
				self.move = 2
			else:
				self.move = 0

		# if I win
		elif self.move == 1 and move == 0: # I play paper they play rock
			if max(self.dic, key = self.dic.get) == move: # if their most played move is rock then play paper again
				self.move = 1
			else:
				self.move = random.choice([move,2]) # play either their move or what would be the next move in the series
		elif self.move == 2 and move == 1: # I play scissors they play paper
			if max(self.dic, key = self.dic.get) == move: # if their most played move is paper then play scissors again
				self.move = 2
			else:
				self.move = random.choice([move,0]) # play either their move or what would be the next move in the series
		elif self.move == 0 and move == 2: # I play rock they play scissors
			if max(self.dic, key = self.dic.get) == move: # if their most played move is scissors then play rock again
				self.move = 0
			else:
				self.move = random.choice([move,1]) # play either their move or what would be the next move in the series

		# if I lose copy their last move
		else:
			self.move = move


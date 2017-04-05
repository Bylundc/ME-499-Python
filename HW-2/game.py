#!/usr/bin/env python


from rps import *
import bylundc
import test



if __name__ == '__main__':
	bylundc = bylundc.MyPlayer()
	test = test.MyPlayerTest()

	players = [Obsessive(), Random(), TitForTat(), bylundc]
	
	i = 0
	for i in xrange(10):
		tournament(players, 10000, False)
		tournament(players, 10000, True)
		i += 1

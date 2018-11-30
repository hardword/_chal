#!/bin/python
#Detecting ECB Mode
from collections import defaultdict

def chunked_list(hexstring, keysize):
	chunked_list = []
	keysize = keysize * 2 #hexstring
	for i in xrange(len(hexstring)/keysize):
		chunked_list.append(hexstring[i*keysize:(i+1)*keysize])
	# padding: can be ignored in this case
	# if len(hexstring) % keysize != 0:
	#	 cl.append(hexstring[(-1 * (len(hexstring) % keysize)):].zfill(keysize))
	return chunked_list

blockSize=16
f = open("cp1-8.txt","ro")
ecb_list = []
for l in f.readlines():
	cl = chunked_list(l, blockSize)
	cd = defaultdict(int)
	for i in cl:
		cd[i] += 1
		if cd[i] > 1:
			ecb_list.append(l)

print set(ecb_list)
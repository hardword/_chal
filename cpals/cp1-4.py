#!/bin/python
import codecs

def isPrintable(hexstring):
	result = True
	for i in xrange(len(hexstring)/2):
		idx = i*2
		chx = hexstring[idx:idx+2]
		if int(chx, 16) < 32 or int(chx, 16) > 127:
				# control character exceotions: NUL, LF, CR
				if int(chx, 16) in [0, 10, 13]:
					pass
				else:
					result = False
					break
	return result

f = open("cp1-4.txt", "ro")
for hexstring in f.readlines():
	hexstring = hexstring.strip()
	byte = len(hexstring)/2
	for i in xrange(128):
		key = format(i, 'x').zfill(2)*byte
		xored = format(int(hexstring, 16)^int(key, 16), 'x').zfill(len(hexstring))
		if isPrintable(xored):
			print codecs.decode(xored, "hex")



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

hexstring = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
byte = len(hexstring)/2
for i in xrange(128):
	key = format(i, 'x').zfill(2)*byte
	xored = format(int(hexstring, 16)^int(key, 16), 'x').zfill(len(hexstring))
	if isPrintable(xored):
		print "key:"+format(i,'x').zfill(2)+" -> "+codecs.decode(xored, "hex")
	


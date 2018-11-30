#!/bin/python
from base64 import b64decode
from itertools import combinations
from itertools import product
#from langdetect import detect
from operator import itemgetter
from codecs import decode
import enchant

#isPrintable
def isPrintable(hexstring):
	result = True
	for i in xrange(len(hexstring)/2):
		idx = i*2
		chx = hexstring[idx:idx+2]
		if int(chx, 16) < 32 or int(chx, 16) > 127:
				# control character exceotions: LF, CR
				if int(chx, 16) in [10, 13]: #Removing NUL from [0, 10, 13]
					pass
				else:
					result = False
					break
	return result

#chunked_list_without_padding
def chunked_list(hexstring, keysize):
	chunked_list = []
	keysize = keysize * 2 #hexstring
	for i in xrange(len(hexstring)/keysize):
		chunked_list.append(hexstring[i*keysize:(i+1)*keysize])
	# padding: can be ignored in this case
	# if len(hexstring) % keysize != 0:
	#	 cl.append(hexstring[(-1 * (len(hexstring) % keysize)):].zfill(keysize))
	return chunked_list

# retrieve hex string
f = open("cp1-6.txt","ro")
ds = ''.join(f.read().strip().split('\n'))
hs = b64decode(ds).encode("hex")

# determining key size (between 2 and 40 as suggested)
min_keysize = 2
max_keysize = 40

kd = {} #key_size_&_distance_dictionary
for ks in xrange(min_keysize, max_keysize+1):
	dl = [] #distance_b/w_2_chunks_combination_list
	cl = chunked_list(hs,ks)
	# calculating hamming distance for every combinations
	for j in combinations(cl, 2):
		dl.append(bin(int(j[0], 16)^int(j[1], 16)).count('1') / float(ks)) # floay(ks) for normalization
	kd[ks] = reduce(lambda x, y: x + y, dl) / len(dl) # average of all hamming distances
# sorting dictionary per value
sorted_kd = sorted(kd.items(), key=itemgetter(1))

# transposing the blocks per key size (try 5 keys with the smallest distance)
# to do : zip(*list) ?? 
num_key_sizes_to_try = 5

ksl = []
# ksl = [29, 18, 36, 25, 12]
for i in xrange(num_key_sizes_to_try):
	ksl.append(sorted_kd[i][0])

# key candidate dictionary
kcd = {}
for ks in ksl:
	# hs: hexstring, ks: keysize
	cl = chunked_list(hs,ks)
	tl = []
	# transposing the blocks(chunks) per key size, ks
	for i in xrange(len(cl)):
		c = cl[i]
		for j in xrange(ks):
			if i == 0:
				tl.append(c[j*2:(j+1)*2])
			else:
				tl[j] += c[j*2:(j+1)*2]
	# key candidate dictionary with position as key and candidate characters' list as a value
	kd = {}
	for i in xrange(len(tl)):
		t = tl[i]
		kd[i] = []
		byte = len(t)/2
		# assuming the key is w/o control characters
		# break each block as single-chracter XOR
		for j in xrange(32,127):
			key = format(j, 'x').zfill(2)*byte
			xored = format(int(t, 16)^int(key, 16), 'x').zfill(len(t))
			if isPrintable(xored):
				kd[i].append(chr(int(format(j,'x').zfill(2),16)))
	kl = []
	for i in xrange(len(kd)):
		kl.append(kd[i])
	if [] not in kl:
		kcd[ks] = kl

for i in kcd:
	m = i
	if i > 15:
		m = 15
	keylist = list(product(*kcd[i][0:m]))
	for t in keylist:
		key = ''.join(t)
		hkey = key.encode("hex")
		enc = hs[0:m*2]
		dec = format(int(hkey, 16)^int(enc, 16), 'x')
		if isPrintable(dec):
			txt = decode(dec, "hex")
			#if detect(txt) == 'en':
			words = txt.split()
			d = enchant.Dict("en_US")
			if len(words) > 1 and len(words[0])+len(words[1]) > 2:
				if d.check(words[0]) and d.check(words[1]):  
					print key + " -> " + txt

# Could find the first 15 characters of the key
# Terminator X: B -> I'm back and I'
# Manual From Here
# Answer: "Terminator X: Bring the noise"
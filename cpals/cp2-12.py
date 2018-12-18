#!/bin/python

from base64 import b64decode
from Crypto.Cipher import AES
from Crypto import Random
import random

def pad_PKCS7(msg, block_size):
	# num_blocks = (len(msg) / block_size) + 1
	pad_size = block_size - (len(msg) % block_size)
	pad = chr(pad_size)*pad_size
	return msg + pad

def unpad_PKCS7(msg):
	return msg[:-ord(msg[-1])]

def aes_ecb_enc(pt, key):
	#key = Random.new().read(block_size)
	cipher = AES.new(key, AES.MODE_ECB)
	#return b64encode(cipher.encrypt(pt))
	return cipher.encrypt(pt)


def cbc_or_ecb(ct, block_size):
	ct_blocks = []
	for i in xrange(len(ct)/block_size):
		init = i*block_size
		ct_blocks.append(ct[init:init+block_size])
	if len(ct_blocks) - len(set(ct_blocks)) <= (len(ct)/block_size)*0.01:
		return "CBC"
	else:
		return "ECB"

block_size = 16
key = Random.new().read(block_size)

def oracle_enc1(pt=''):
    unknown_string = b64decode(
        "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\n" +
        "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\n" +
        "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\n" +
        "YnkK")
    pt = pad_PKCS7(pt + unknown_string, block_size)
    return aes_ecb_enc(pt, key)

def get_block_size():
	n = 1
	default_len = len(oracle_enc1())
	while True:
		blocksize = len(oracle_enc1(chr(255)*n)) - default_len
		if blocksize:
			return blocksize
		n += 1

blocksize = get_block_size()
print "Block Size:", blocksize

pt = chr(255) * 1000
ct = oracle_enc1(pt)
mode = cbc_or_ecb(ct, blocksize)
print "Mode:", mode


known_string = ''

num_blocks = len(oracle_enc1(known_string))/blocksize

for h in xrange(num_blocks):
	b_start = h*blocksize
	b_end = h*blocksize+blocksize
	for i in xrange(1, blocksize+1):
		pt = (chr(255) * (blocksize - i))
		ct = oracle_enc1(pt)
		for j in xrange(0,127):
			cmp_pt = (chr(255) * (blocksize - i)) + known_string + chr(j)
			cmp_ct = oracle_enc1(cmp_pt)
			if ct[b_start:b_end] == cmp_ct[b_start:b_end]:
				known_string += chr(j)
				break

print "\nUnknown String: "			
print unpad_PKCS7(known_string)
	

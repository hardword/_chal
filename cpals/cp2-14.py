#!/bin/python
#Think "STIMULUS" and "RESPONSE"

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

block_size = 16
key = Random.new().read(block_size)
random_prefix = Random.new().read(random.randint(0,255))

def oracle_enc2(pt=''):
	unknown_string = b64decode(
		"Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\n" +
		"aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\n" +
		"dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\n" +
		"YnkK")
	pt = pad_PKCS7(random_prefix + pt + unknown_string, block_size)
	return aes_ecb_enc(pt, key)

def get_block_size():
	n = 1
	default_len = len(oracle_enc2())
	while True:
		blocksize = len(oracle_enc2(chr(255)*n)) - default_len
		if blocksize:
			return blocksize
		n += 1

def get_prefix_info():
	bs = get_block_size()
	ct = oracle_enc2(chr(255)*48)
	num_blocks = len(ct)/bs
	p_block = ''
	block_cnt = 0
	for i in xrange(num_blocks):
		c_block = ct[i*bs:i*bs+bs]
		if p_block != c_block:
			p_block = c_block
			block_cnt += 1
		else:
			break
	block_cnt -= 1
	last_block = ct[0:block_cnt * bs][-bs:]
	for j in xrange(bs):
		com_ct = oracle_enc2(chr(255)*j)
		if last_block == com_ct[0:block_cnt * bs][-bs:]:
			break
	return {'size': block_cnt * bs - j, 'pad': j, 'blockcount': block_cnt, 'blocksize': bs}

prefix = get_prefix_info()
print prefix

base_string = chr(255) * prefix['pad']
blocksize=prefix['blocksize']
num_blocks = len(oracle_enc2(base_string))/blocksize
known_string = ''

for h in xrange(prefix['blockcount'],num_blocks):
	b_start = h*blocksize
	b_end = h*blocksize+blocksize
	for i in xrange(1, blocksize+1):
		pt = base_string + (chr(255) * (blocksize - i))
		ct = oracle_enc2(pt)
		for j in xrange(0,127):
			cmp_pt = base_string + (chr(255) * (blocksize - i)) + known_string + chr(j)
			cmp_ct = oracle_enc2(cmp_pt)
			if ct[b_start:b_end] == cmp_ct[b_start:b_end]:
				known_string += chr(j)
				break

print "\nUnknown String: "			
print unpad_PKCS7(known_string)


	

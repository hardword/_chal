#!/bin/python
#Think "STIMULUS" and "RESPONSE"

from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto import Random
import random

# PreProcess
block_size = 16
key = Random.new().read(block_size)
iv = Random.new().read(16)

def pad_PKCS7(msg, block_size):
	# num_blocks = (len(msg) / block_size) + 1
	pad_size = block_size - (len(msg) % block_size)
	pad = chr(pad_size)*pad_size
	return msg + pad

def unpad_PKCS7(msg):
	return msg[:-ord(msg[-1])]

def aes_cbc_enc(pt, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return cipher.encrypt(pt)

def aes_cbc_dec(ct, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return cipher.decrypt(ct)

def oracle_enc3(pt = ''):
	prefix = "comment1=cooking%20MCs;userdata="
	suffix = ";comment2=%20like%20a%20pound%20of%20bacon"
	pt = pt.replace(';','%3b').replace('=','%3d')
	#print "Plaintext:", pt
	pt = pad_PKCS7(prefix + pt + suffix, block_size)
	return aes_cbc_enc(pt, key, iv)

def is_admin(ct):
	pt = aes_cbc_dec(ct, key, iv)
	return ";admin=true;" in pt

def get_block_and_pad_size():
	padsize = 1
	default_len = len(oracle_enc3())
	while True:
		blocksize = len(oracle_enc3(chr(255)*padsize)) - default_len
		if blocksize:
			return [blocksize, padsize]
		padsize += 1

def split_string(str, length=1):
	result = []
	if len(str) % length == 0:
		num_blocks = len(str)/length 
	else:
		num_blocks = len(str)/length + 1
	for i in xrange(num_blocks):
		start = i * length
		end = i * length + length
		try:
			block = str[start:end]
		except IndexError:
			block = str[start:]
		result.append(str[start:end])
	return result


s = oracle_enc3()
l = split_string(s, 16)
for b in l:
	print b.encode('hex')
l = split_string('ddd', 4)
print l

'''
def get_default_text_length():
	enc_len_with_pad = len(oracle_enc3())
	m, n = map(int, get_block_and_pad_size())
	return enc_len_with_pad - n
'''



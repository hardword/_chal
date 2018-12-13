#!/bin/python

from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto import Random
import random
import Padding

def pad_PKCS7(msg, block_size):
	# num_blocks = (len(msg) / block_size) + 1
	pad_size = block_size - (len(msg) % block_size)
	pad = chr(pad_size)*pad_size
	return msg + pad

def unpad_PKCS7(msg):
	return msg[:-ord(msg[-1])]

def aes_cbc_enc_randomkey(pt, block_size):
	iv = Random.new().read(block_size)
	key = Random.new().read(block_size)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	#return b64encode(cipher.encrypt(pt))
	return cipher.encrypt(pt)

def aes_ecb_enc_randomkey(pt, block_size):
	key = Random.new().read(block_size)
	cipher = AES.new(key, AES.MODE_ECB)
	#return b64encode(cipher.encrypt(pt))
	return cipher.encrypt(pt)

def mod_pt(pt):
	a = Random.new().read(random.randint(5,10))	
	b = Random.new().read(random.randint(5,10))
	return a + pt + b

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
mode = random.randint(1,2)
f = open("cp2-11.txt", "ro")
pt = f.read()
pt = mod_pt(pt)
pt = pad_PKCS7(pt, block_size)

print "PT Length: ", len(pt)

if mode == 1:
	print "Mode: CBC"
	ct = aes_cbc_enc_randomkey(pt, block_size)
else:
	print "Mode: ECB"
	ct = aes_ecb_enc_randomkey(pt, block_size)

print "Guess:", cbc_or_ecb(ct, block_size)

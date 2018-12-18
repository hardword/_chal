#!/bin/python
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
import Padding

def pad_PKCS7(msg, block_size):
	# num_blocks = (len(msg) / block_size) + 1
	pad_size = block_size - (len(msg) % block_size)
	pad = chr(pad_size)*pad_size
	return msg + pad

def enc(pt, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return cipher.encrypt(pt)

def dec(ct, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return cipher.decrypt(ct)

key_raw = 'YELLOW SUBMARINE'
block_size = len(key_raw)
iv = chr(0) * block_size
#f = open("cp2-10.txt","ro")
#enc_b64 = ''.join(f.read().strip().split('\n'))
#enc_raw = b64decode(enc_b64)

#print Padding.removePadding(pt, blocksize=block_size, mode='CMS')
#print Padding.removePadding(pt, mode=0)

pt = "Well that's my DJ Deshay cuttin' all them Z's"
#pt = pad_PKCS7(pt, block_size)
pt = Padding.appendPadding(pt, mode=0)

enc_b64 = enc(pt, key_raw, iv)
enc_raw = b64decode(enc_b64)

pt = dec(enc_raw, key_raw, iv)
pt = Padding.removePadding(pt, mode=0)

print enc_b64
print pt


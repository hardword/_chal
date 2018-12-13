#!/bin/python

def pad_PKCS7(msg, block_size):
	# num_blocks = (len(msg) / block_size) + 1
	pad_size = block_size - (len(msg) % block_size)
	pad = chr(pad_size)*pad_size
	return msg + pad

def unpad_PKCS7(msg):
	return msg[:-ord(msg[-1])]

def validate_PKCS7(msg, block_size):
	last_block = msg[-block_size:]
	pad_size = ord(last_block[-1:])	
	return last_block[-1]*pad_size == last_block[-pad_size:]

msg = "YELLOW SUBMARINE"
msg = pad_PKCS7(msg, 20)
print validate_PKCS7(msg, 20)
print msg

msg = unpad_PKCS7(msg)
print msg

msg = ["ICE ICE BABY\x04\x04\x04\x04", "ICE ICE BABY\x05\x05\x05\x05", "ICE ICE BABY\x01\x02\x03\x04"]
for m in msg:
	print validate_PKCS7(m, 16)
	if validate_PKCS7(m, 16):
		print unpad_PKCS7(m)






#!/bin/python

from Crypto.Cipher import AES
from Crypto import Random

block_size = 16
key = Random.new().read(block_size)

def pad_PKCS7(msg, block_size):
	# num_blocks = (len(msg) / block_size) + 1
	pad_size = block_size - (len(msg) % block_size)
	pad = chr(pad_size)*pad_size
	return msg + pad

def unpad_PKCS7(msg):
	return msg[:-ord(msg[-1])]

def aes_ecb_enc(pt, key):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.encrypt(pt)

def aes_ecb_dec(ct, key):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.decrypt(ct)

def urlquery_to_dict(param):
	obj = {}
	for kv in param.split('&'):
		kv = kv.split('=')
		obj[kv[0]] = kv[1]
	return obj

#print urlquery_to_dict("foo=bar&baz=qux&zap=zazzle")

def profile(email, uid='10', role='user'):
	obj = {}
	user_id, user_role = uid, role
	if all(['&' not in email, '=' not in email]):
		obj['email'] = email
		obj['uid'] = user_id
		obj['role'] = user_role
	return obj

"""
def dict_to_urlquery(obj):
	qs = ''
	for key in obj:
		qs += (key + '=' + obj[key] + '&')
	return qs[:-1]
"""
def profile_to_urlquery(obj):
	return 'email='+obj['email']+'&uid='+obj['uid']+'&role='+obj['role']	


def profile_for(email=''):
	pt = pad_PKCS7(profile_to_urlquery(profile(email)),len(key))
	ct = aes_ecb_enc(pt, key)
	return ct

def decrypt_profile(ct, key):
	pt = aes_ecb_dec(ct, key)
	pt = unpad_PKCS7(pt)
	return pt

def get_block_size():
	n = 1
	default_len = len(profile_for())
	while True:
		blocksize = len(profile_for(chr(255)*n)) - default_len
		if blocksize:
			return blocksize
		n += 1

def create_admin_profile():
	bs = get_block_size()
	#get the first block of enc
	base = 'email=&uid=10&role='
	for i in xrange(bs): 
		if (len(base)+i)%bs == 0:
			break
	email = "A"*i
	ct_first = profile_for(email)
	num_blocks = len(ct_first)/bs
	ct_first_part = ct_first[:-bs]
	#get the second block of enc
	base = 'email='
	for i in xrange(bs): 
		if (len(base)+i)%bs == 0:
			break
	email = "A"*i
	#string 'admin' only in the next block 
	email += pad_PKCS7('admin', bs)
	ct_second_part = profile_for(email)[bs:bs*2]
	return ct_first_part+ct_second_part

print decrypt_profile(create_admin_profile(),key)

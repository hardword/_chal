#!/bin/python
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
import Padding

key_raw = 'YELLOW SUBMARINE'
#key_hex = key_raw.encode("hex")
#print "KEY: "+key_hex

f = open("cp1-7.txt","ro")
enc_b64 = ''.join(f.read().strip().split('\n'))
enc_raw = b64decode(enc_b64)
#enc_hex = b64decode(enc_b64).encode("hex")
#print "ENC: "+enc_hex

# NO_IV!!!
cipher = AES.new(key_raw, AES.MODE_ECB)
dec = cipher.decrypt(enc_raw)
print Padding.removePadding(dec, blocksize=16, mode='CMS')
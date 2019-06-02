import hashlib

from hashlib_data import decript

h = hashlib.md5()
h.update(decript.encode('utf-8'))
print(h.hexdigest())

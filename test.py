from ctypes import *

print(c_int(42))
libc = CDLL("libc.so.6")
print(libc)
print(libc.printf)

from ctypes import *

c_int(42)
libc = CDLL("libc.so.6")
libc.printf

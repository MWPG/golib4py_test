import ctypes
add = ctypes.CDLL('./libadd.so').add

# 显式声明参数和返回的期望类型
add.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
add.restype = ctypes.c_char_p
left = b"Hello"
right = b"World"
print(add(left, right))

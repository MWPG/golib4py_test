import ctypes
add = ctypes.CDLL('./libadd.so').add

# 显式声明参数和返回的期望类型
add.argtypes = [ctypes.c_double, ctypes.c_double]
add.restype = ctypes.c_double
print(add(3.5, 4.6))

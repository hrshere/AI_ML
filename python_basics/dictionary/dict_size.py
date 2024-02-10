'''getting size of dict in bytes'''
import sys

dic1 = {"A":1, "B": 2, "C": 3}
print("size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")
print("size of dic1:" + str(dic1.__sizeof__()) + "bytes")
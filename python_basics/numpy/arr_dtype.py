'''i,b,u,f,c,m,M,o,S,U,V'''
import numpy as np
#arr.dtype- get the data type of array
arr = np.array([1])
print(arr.dtype)

#create with specified dtype
arr_str = np.array([1,2,3,4], dtype='S')
print(arr_str[0])
print(arr_str.dtype)
arr_str2 = np.array(['apple', 'banana', 'cherry'])
print(arr_str2)
print(arr_str2.dtype)

# arr_int = np.array(['a', '2', '3'], dtype='i')#ValueError as ele cant be converted to integer

#converting existing data type
arr2 = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
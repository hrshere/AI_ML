'''access by index'''
import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr[0])
print(arr[:])

#add 3rd and 4th ele
print(arr[2] + arr[3])
print(arr[1:5])
print(arr[-5:-1])
print(arr[1:5:2])#step

#2-D array
array_two = np.array([[1,2],[3,4]])
print('2nd element of 1st row:', array_two[0,1])#print ele
print('2nd element of 1st row:', array_two[0,1:2])#prints a list
print(array_two[0:2,0:1])#[[1][3]]


#3-D array
array_three = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[6,5,4]]])
print(array_three[0,1,2])
print(array_three[0:1,1:2,2:3])

#print last ele from array_two
print(f'last ele from array_two: {array_two[1, -1]}')


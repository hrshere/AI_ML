numbers = [10,20,[300,400,[5000,6000],500],30,40]
# numbers[2][2][2] = 9000
# numbers = numbers.insert(9000,numbers[2][2][1]+1)
# print(numbers)
print(numbers[2][2][1])
# index_1 = numbers.index(numbers[2][2][1])
# numbers = numbers.insert(9000, index_1+1)
print(numbers)

index = [2][2][2]

numbers.insert(index,9000)
print(numbers)

# #how to find index of a given element in list
# for i in range(len(numbers)):
#     if numbers[i] == 6000:
#         print(i)
#     else:
#         print('not found')
# # or how to find if a given element is present in a nested list
# num1 = [2,3,[4]]
# print(num1)
# for i in range(len(num1)):
#     if num1[i] == [4]:
#         print(i)

numbers[2][2].append()
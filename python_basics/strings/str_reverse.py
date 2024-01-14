'''take input from user and reverse '''

input = input('enter some string')
# input = input [::-1] slicing
# input = ''.join(reversed(input)) 

#using for loop
reversed_string = ''
for i in range(len(input)-1,-1,-1):
    reversed_string += input[i]
print(reversed_string)
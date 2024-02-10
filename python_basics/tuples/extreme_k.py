'''
max and min k elements in a tuple:
Input : test_tup = (3, 7, 1, 18, 9), k = 2 
Output : (3, 1, 9, 18)

Input : test_tup = (3, 7, 1), k=1 
Output : (1, 7) 
'''

test_cup = (3,7,1,18,9)
k = 2
if len(test_cup) == 0:
    print("empty tuple")
else:
    for i in test_cup:
        if i>k:
            print(i)
    

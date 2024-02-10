'''
syntax
newlist = [expression for item in iterable if condition == True]
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

orange_not_banana = [x if x != "banana" else "orange" for x in fruits]
print(orange_not_banana)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

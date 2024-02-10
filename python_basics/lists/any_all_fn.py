'''The any() function returns True if any item in an iterable are true, otherwise it returns False.'''
'''if empty obj ret false list,tuple,dict'''
mylist = [False, True, False]
x = any(mylist)
print(x)

'''all fn ret true is all itms of iterable are true'''
x = all(mylist)
print(x)

'''ex'''
def main():
    print(has_lucky_number([1,2,3,4]))
    print(has_lucky_number_py([1,2,7]))

def has_lucky_number(nums):
    """Returns whether the given list of numbers is lucky.
    A lucky no. contains atleast one no div by 7"""
    for num in nums:
        if num % 7 == 0:
            return True
    #after list is exhausted without finding 
    return False

def has_lucky_number_py(nums):
    return any([num % 7 == 0 for num in nums])

if __name__ == "__main__":
    main()


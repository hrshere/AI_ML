# names = ['carter','john','henry']

# name = input('enter name : ')

# if name in names:
#     print('found')
# else:
#     print('DNE')
 
'''return 1st position if v in l else return -1 -- buggy'''

# def FindPos(l,v):
#     print(len(l))
#     (found, i) = (False, 0)
#     while i < len(l):
#         print(i)
#         if l[i] == v:
#             (found,pos) = (True,i)
#         else:
#             i += 1
#     if not found:
#         pos = - 1
#     return(pos)
    
# print(FindPos([1,2],2))

'''a more natural strategy'''
def findpos(l,v):
    (pos, i) = (-1, 0)
    for x in l:
        if x == v:
            pos = i
            break
        i = i+1
    return(pos)

y = findpos([1,2,2,3],5)
print(y)

'''
linear search -- seq(array/list)
   worst case - time proportional to length of list
'''
def search(seq,v):
    for x in seq:
        if x == v:
            return True
        else:
            return False

'''
what is seq is sorted? -- Binary Search
    > compare v with midpoint of seq
    > if midpoint is v, the value is found
    > if v < midpoint, search left half of seq
    > else search right half of the seq
'''
def bsearch(seq,v,l,r):
    pass
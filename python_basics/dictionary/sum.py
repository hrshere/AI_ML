'''find the sum of all items in the dictionary'''
dict = {'a':100,'b':200,'c':300}
sum = sum(dict.values())
print(sum)

def returnSum(myDict):
    return sum(myDict[key] for key in myDict)

print(returnSum(dict))
'''potential issue fn name used as variable'''
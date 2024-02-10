'''sort python dictionaries by key or value'''

#create a dict
myDict = {'ravi':10, 'raj': 9, 'yash':32}
 
#convert keys to list
myKeys = list(myDict.keys())

#sort list of keys alphabetically
myKeys.sort()

#display both the keys and values sorted by value in alphabetical order
sorted_dict = {i: myDict[i] for i in myKeys}
print(sorted_dict)

'''m2 - using function'''
def dictionary():
    key_value = {}

    key_value[2] = 56
    key_value[1] = 20
    key_value[3] = 33
    key_value[4] = 44
    key_value[5] = 55

    print("key_value", key_value)

    for i in sorted(key_value.keys()):
        print(i, end= " ")
    print(dict(sorted(key_value.items())))

def main():
    dictionary()

if __name__ == "__main__":
    main()


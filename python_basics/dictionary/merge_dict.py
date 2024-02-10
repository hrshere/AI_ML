'''
merging two dictionaries:
'''

def main():
    dict1 = {"a": 10}
    dict2 = {"b": 20}
    print(merge(dict1,dict2))

#using update method
def update_merge(dict1,dict2):
    return(dict1.update(dict2))

#using unpacking operator
def unpacking_merge(dict1,dict2):
    res = {**dict1, **dict2}
    return res

#using key merge
def key_merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1

def merge(dict1,dict2):
    res = dict1 | dict2
    return res

if __name__ == "__main__":
    main()

'''
Dictionaries store key:value pairs
ordered:- items have a defined order, and that order will not change
unordered:- cannot refer to an item by using an index
changable- can change , add or remove items after the dict has been created
duplicates not allowed
'''
my_dict = {'one': 1, 'three': 3, 'two': 2}
print("Original Dictionary", my_dict)

my_dict['four'] = 4
print(f"Modified Dictionary:", my_dict)

'''to show that order of insertion is mantained'''
for key, value in my_dict.items():
    print(f"{key}: {value}")

'''to show that duplicate values will overwrite existing values'''
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
print(len(thisdict))#to get length of dictionary

'''dict() constructor'''
my_constructed_dict = dict(name = "John", age = 36, country = "Norway")
print(my_constructed_dict)

'''Accessing items'''
#access items of a dictionary by referring to its key name, inside square brackets:
x = thisdict["model"]
print(x)#prints value
#m2 get() method
year = thisdict.get("year")
print(year)

'''Get Keys'''
#using keys() method - gets a list of keys
keys = thisdict.keys()
print(keys)

'''Get Values'''
#values() method return list of all the values in the dictionary

values = thisdict.values()
print(values)

'''Get Items'''
#items() method will return each item in a dictionary, as tuples in a list

items = thisdict.items()
print(items)

'''check if key exists'''
#in keyword
if "model" in thisdict:
    print("Yes model is one of the keys in thisdict")

'''change values'''
thisdict["year"] = 2018

'''update dictionary'''
#update method - update the dict with the item from the given arg
#arg must be a dict, or an iterable obj with k:v pairs

thisdict.update({"year": 2024})

'''nest dictionary'''
score = {}
score["Test1"] = {}
score["Test2"] = {}
score["Test1"]["Kolhi"] = 109
score["Test1"]["Dhawan"] = 101
score["Test2"]["Kolhi"] = 98
score["Test2"]["Dhawan"] = 177
print(score)

'''removing items'''
#pop method removes items with specified key name:
thisdict.pop("model")
print(thisdict)

#popitem method removes the last inserted item
thisdict["purchase"] = 'done'
print(thisdict)
thisdict.popitem()
print(thisdict)

#del keyword removes the item with the specified key name
#can also delete the dict completely
del thisdict["brand"]
print(thisdict)

#clear() method empties the dictionary


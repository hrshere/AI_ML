'''sort list of dictionaries by values in python'''
from operator import itemgetter

list = [{"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikil", "age": 19}]

#using itemgetter
print(sorted(list, key=itemgetter('name')))

#using lambda fn
print(sorted(list, key=lambda i: i['age']))
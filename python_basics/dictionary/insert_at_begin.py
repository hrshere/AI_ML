'''
insert item at beginning of dict
'''
dict1 = {"a":20,"b":30}
to_be_inserted = {"c":40}
#expected {"c":40,"a":20,"b":30}

#trick1
to_be_inserted.update(dict1)
print(to_be_inserted)

#trick2 -- unpacking items
res = {**to_be_inserted, **dict1}
print(res)

from collections import OrderedDict

iniordered_dict = OrderedDict([("a", 20), ("b", 30)])
iniordered_dict.update({"c":40})
iniordered_dict.move_to_end("c", last = False)

print(str(iniordered_dict))

#using for loop
for i in list(dict1.keys()):
    to_be_inserted[i] = dict1[i]
print(to_be_inserted)
'''ways to remove a key from dictionary'''

test_dict = {'hrs': 'Himanshu',"kv":'kushal'}
#m1
new_dict = {key: val for key, val in test_dict.items() if key != 'hrs'}
#m2
new_dict2 = test_dict.pop('hrs')
#m3
new_dict3 = {key: test_dict[key] for key in test_dict in test_dict if key != "hrs"}
print(new_dict3)
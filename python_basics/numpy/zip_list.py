import numpy as np

test_list1 = ['W', "will", "quit","learning"]
test_list2 = ['e', 'not', 'without', 'python']

arr1 = np.array(test_list1)
arr2 = np.array(test_list2)
print(arr1)

# concatenated_arr = np.concatenate((arr1, arr2))
# concatenated_arr = np.core.defchararray.add(arr1, arr2) #deprecated - backward compatibailty
concatenated_arr = np.char.add(arr1,arr2)

res = concatenated_arr.tolist()

print("The modified zipped list is:", res)
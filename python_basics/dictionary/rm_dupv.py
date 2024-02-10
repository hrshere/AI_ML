'''remove duplicate values across dictionary values'''

test_dict = {'Manjeet': [1,4,5,6],
             'Akash': [1,8,9],
             'Nikhil': [10,22,4],
             'Akshat': [5,11,22]}

print("The original dictionary : " + str(test_dict))

x = []
for i in test_dict.keys():
    x.extend(test_dict[i])
print(x)#storing all values in x

y = []
for i in x:
    if(x.count(i) == 1):
        y.append(i)
print(y)#finding values that occur only once

res = dict()
for i in test_dict.keys():
    a = []
    for j in test_dict[i]:
        if j in y:
            a.append(j)
        res[i] = a

print("Uncommon elements records :" + str(res))
'''in - list membership -- safely remove l from x'''
x = [1,2,3,2,4]
l = 2
for i in range(len(x)):
    if l in x:
        x.remove(l)
print(x)

#method 2
while l in x:
    x.remove(l)

list1 = ["Jan","", "Feb", "May","","jun"]
x = ""
while x in list1:
    list1.remove(x)

print(list1)
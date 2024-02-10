list1 = ["Jan","", "Feb", "May","","jun"]
i = 0
for i in range(len(list1)):

    if(list1[i]==""):
        list1.pop(i)
        # list1 = list1.pop(i)

print(list1)

# list1 = [item for item in list1 if item != ""]
# print(list1)

# i = 0
# while i < len(list1):
#     if list1[i] == "":
#         list1.pop(i)
#     else:
#         i += 1

# print(list1)
#filter


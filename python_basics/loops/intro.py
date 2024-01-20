'''loops concept'''

i = 0
while i < 3:
    print("meow")
    i += 1
    #python do not support ++ 

#poor design list
for i in [0,1,2]:
    print("meow")

#pythonic
for _ in range(3):
    print("meow")

#more efficient
print("meow" * 3)

#getting user input -- validating input
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

#iterating with lists
students = ['a','b','c']
for student in students:
    print(student)

for student in range(len(students)):
    print(student)

#dict
students_dict = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students_dict:
    print(student)#prints index by default (key)
    print(students_dict[student])#value

# dict with multiple key -values associated can be implemented as list

students_dict_list = [
    {"name": "h", "house": "hh", "place":"hhh"},
    {"name": "i", "house": "ii", "place":"iii"},
    {"name": "j", "house": "jj", "place": "jjj"}
]
for student in students_dict_list:
    print(student["name"],student["house"],student["place"])

"""a constant list of dictionary for person name and number"""

people = [
    {"name": "Carter", "number": "+1-111-1111"},
    {"name": "David", "number": "+1-222-2222"},
    {"name": "John", "number": "+1-333-3333"}
]

#search for name
name = input("Name: ")
for person in people:
    if person["name"] == name:
        print(f"found {person['number']}")
        break
else:
    print("Not found")

# add contacts
    
# delete contacts
    
# update contacts
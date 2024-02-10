country_dict = {
    "India": "New Delhi",
    "America": "New York",
    "Russia": "Moscow"
}

#print keys one by one
for item in country_dict:
    print(item)

#print values
for item in country_dict:
    print(country_dict[item])

print(country_dict.items())

#print key , value one by one
for item in country_dict:
    print(f"key: {item} => value: {country_dict[item]}")
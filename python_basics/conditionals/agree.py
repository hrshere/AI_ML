
s = input("Do you agree?").lower().strip()

if s in ["y",  "yes"]:
    print("Agreed")
elif s in ["n", "no"]:
    print("Not Agreed")
else:
    print('wrong response')
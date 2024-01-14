"""comparing two values"""

while True:
    try:
        x = int(input("Enter first value: "))
        break
    
    except ValueError:#if any value other than integer is entered by user
        print("Not an integer")

while True:
    try:
         y = int(input("Enter second value: "))
         break
    except ValueError:
        print("Not an integer")

if x > y:
    print("1st value is greater")
elif x < y:
    print("2nd value is greater")
else:
    print("Both the numbers are")
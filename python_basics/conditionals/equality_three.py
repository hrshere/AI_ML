"""compare three values"""

while True:
    try:
        x = int(input('x: '))
        break
    except ValueError:
        print('not an integer')

while True:
    try:
        y = int(input("y: "))
        break
    except ValueError:
        print('Not an integer')

while True:
    try:
        z = int(input('z: '))
        break
    except ValueError:
        print('Not an integer')

if x > y:
    if x > z:
        print('x is largest of the three')
    else:
        print('z is largest of the three')
elif x < y:
    if y > z:
        print('y is largest of the three')
    else:
        print('z is largest of the three')
else:
    print('All the three numbers are same')
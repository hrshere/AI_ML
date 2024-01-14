# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

while True:
    try:
        n = int(input('n: '))
        break
    except ValueError:
        print('not an integer')

for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()
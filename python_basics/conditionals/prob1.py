'''find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)'''

x, y, count = 1500, 2700, []
for n in range(x, y+1):
    if n % 7 == 0 and n % 5 == 0:
        count.append(str(n))
# print(count)
print(','.join(count))
        
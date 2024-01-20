x = float(input("Enter x: "))
y = float(input("Enter y: "))

#without using round, with the help of formatted string
z_div = x / y
print(f"{z_div:.2f}")


z = round(x+y)
print(z)

#to present 000 with commas
print(f"{z:,}")

'''convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]'''

while True:
   try:
       c = int(input('Enter temperature in celsius: '))
       break
   except ValueError:
       print('not a number')

f = 9/5*(c) + 32

print(f)

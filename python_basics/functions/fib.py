'''print a fibonacci series upto n'''
def main():
   
    try:
        n = int(input('enter n: '))
        fib(n)
    except ValueError:
        print('Not a number')

def fib(n):
    a, b = 0, 1
    while a<n:
        print(a)
        a, b = b, a+b

main()
'''small anonymous fns created with lambda keyword'''

def main():
    f = make_incrementor(42)
    print(f(3))

def make_incrementor(n):
    '''returns the sum of its two arguments'''
    return lambda x: x + n

main()


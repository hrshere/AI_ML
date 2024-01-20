def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        try:    
            n = int(input('Enter count: '))
            if n > 0:
                return n
            else:
                print('please enter posetive integer')
        except ValueError:
            print('Please enter an integer')

def meow(n):
    for _ in range(n):
        print('meow')

main()
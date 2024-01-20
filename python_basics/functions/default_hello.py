def main():
    to = input('your name: ')
    hello()
    hello(to)

def hello(name="World"):#default arg, if arg provided at time of fn call, it is overridden 
    print(f"hello, {name}")

main()
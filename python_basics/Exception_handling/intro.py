def main():
    x = get_int()
    print(f"x: {x}")

def get_int():
    while True:
        try:
            # x = int(input("what's x? "))
            return int(input("what's x?"))
        except ValueError:
            print('x is not an integer')#pass if do nothing
        else:
            # break
            return x#optimization does work of both
    # return x

main()
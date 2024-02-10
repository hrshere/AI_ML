'''handling missing key'''

def main():
    setdefault_key()

#using try except O(1)
def try_keys():
    d = {'a':1,'b':2}
    while True:
        try:
            i = input('key:')
            print(d[i])
        except KeyError:
            print('key not found')
        else:
            break

#Using membership
def key_memb():
    d = {'a':1,'b':2}
    i = input('enter key')
    if i in d:
    #if i in d.keys()
        print(d[i])
    else:
        print('key not found')

#using get:
def get_key():
    d = {'a':1,'b':2}
    i = input('enter key')
    print(d.get(i))

#setdefault(key, def_value) work as get(), if no key asso, create one
def setdefault_key():
    d = {'a':1,'b':2}
    i = input('enter key')
    print(d.setdefault(i,5))
    print(d)


if __name__ == "__main__":
    main()

        




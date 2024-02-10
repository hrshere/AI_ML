'''reverse string using recursion'''

def main():
    print(reverse('hello'))

def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:])+s[0]
    
if __name__ == "__main__":
    main()
'''check is a string is palindrome'''
def main():
    print(is_palindrome('anna'))

def is_palindrome(phrase):
    print(phrase[::-1])# todo -- concept
    return phrase == phrase[::-1]

if __name__ == "__main__":
    main()
'''a word having same letters as other but different arrangement'''

def main():
    print(is_anagram("elvis", "lives"))

def is_anagram(s1, s2):
    return set(s1) == set(s2)

if __name__ == "__main__":
    main()
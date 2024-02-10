'''to get all the indices in a list for a specified duplicate element'''

def main():
    x = common_index()
    print(x)

def common_index(seq = ("apple","mango","apple")):#buggy
    i = 0
    common = []
    while i < len(seq):
        common.append(seq.index("apple"))
        i += 1
    return common

if __name__ == "__main__":
    main()

def main():
    duplicate_element = "apple"
    indices = common_index(("apple", "mango", "apple"), duplicate_element)
    print(indices)

def common_index(seq, duplicate_element):
    # Use a list comprehension to find all indices of the specified duplicate element
    indices = [i for i, item in enumerate(seq) if item == duplicate_element]
    return indices

def common_index(seq, duplicate_element):
    # Use a list comprehension to find all indices of the specified duplicate element
    indices = [i for i in range(len(seq)) if seq[i] == duplicate_element]
    return indices

if __name__ == "__main__":
    main()
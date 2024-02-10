def main():
    list1 = [2,-3,5,-6,-77]
    print(count_negative1(list1))
    print(count_negative2(list1))
    print(count_negative3(list1))

def count_negative1(list1):
    count = 0
    for value in list1:
        if value<0:
            count += 1
    return count

def count_negative2(list1):
    return len([num for num in list1 if num < 0])

def count_negative3(list1):
    return sum([num < 0 for num in list1])

if __name__ == "__main__":
    main()

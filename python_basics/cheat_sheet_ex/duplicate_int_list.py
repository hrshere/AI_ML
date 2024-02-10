'''find duplicate number in integer list'''
def main():
    l1 = [1,2,2,3,5,3,55,6,8,3,5,2,2]
    p = find_duplicates(l1)
    print(p)

# def find_duplicates(l,v):
#     count = 0
#     for i in range(len(l)):
#         if l[i] == v:
#             count += 1
#     return count
    
def find_duplicates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)

if __name__ == '__main__':
    main()
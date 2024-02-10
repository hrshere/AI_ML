'''remove all duplicates from a list'''

def main():
    lst = list(range(10)) + list(range(10))
    lst = list(set(lst))
    print(lst)
#     p = remove_duplicates([1,2,2,2,3,4])
#     print(p)

# def remove_duplicates(elements):
#     duplicate, seen = set(), set()
#     for element in elements:
#         if element in seen:
#             duplicate.add(element)
#         seen.add(element)
#     for i in duplicate:
#         while i in elements:
#             break if len(elements) == 2 else elements.remove(i)
#             # elements.remove(i)
#     return elements


if __name__ == "__main__":
    main()
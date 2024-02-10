'''
Input: list [1,2,3]
o/p: [(1,1),(2,8),(3,27)]
'''
def main():
    list1 = [1,2,3]
    print(cube_tuple(list1))
    #m2 comprehension
    res = [(list1[i],list1[i]**3) for i in range(len(list1))]
    res2 = [(val, pow(val, 3)) for val in list1]
    print(res2)
    print(res)

#m1
def cube_tuple(seq):
    temp = []
    for i in range(len(seq)):
        temp.append((seq[i],seq[i]**3))
    return temp

#using re
import re
lst_str = "1, 2, 5, 6"
lst = [int(num) for num in re.findall(r'\d+', lst_str)]
result = [(num, num**3) for num in list]
print(result)




if __name__ == "__main__":
    main()
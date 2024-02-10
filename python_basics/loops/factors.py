'''find all the factors of a number n'''
def main():
    n = int(input("Enter n"))
    factors(n)

def factors(n):
    flist = []
    for i in range(1, n+1):
        if n % i == 0:
            flist.append(i)
    print(flist)

main()
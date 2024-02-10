'''Adding Tuple to list and vice versa'''

def main():
    lst = [1,2,3]
    tpl = (4,5)
    print(add_lst_to_tpl(lst,tpl))
    print(add_tuple_to_lst(lst,tpl))

def add_tuple_to_lst(lst,tpl):
    lst += tpl
    return lst

def add_lst_to_tpl(lst,tpl):
    # tpl += lst #TypeError: can only concatenate tuple (not "list") to tuple
    res = tuple(list(tpl) + lst)
    return res

if __name__ == "__main__":
    main()
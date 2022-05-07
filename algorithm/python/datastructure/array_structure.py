import array as arr

def tolist(*args):
    return list(args)

def toarray(target_list: list):
    return arr.array('i', target_list)

if __name__ == "__main__":

    lis = tolist(1, 3, 2, 4, 7, 6, 8, 5)
    print('list')
    print(lis[0])
    print(lis[1])
    print(lis[2])
    print(lis[3])
    print(lis[4])
    print(lis[5])

    a = toarray(lis)
    print('\narray')
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])
    print(a[5])

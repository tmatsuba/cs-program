def merge_sort(arr) -> list:

    if len(arr) <= 1:
        return arr

    pivot = int(len(arr) / 2)
    return merge(merge_sort(arr[:pivot]), merge_sort(arr[pivot:]))


def merge(arr1, arr2) -> list:
    ret = list()
    len1 = len(arr1)
    len2 = len(arr2)

    i = j = 0
    arr1_val = arr1[i]
    arr2_val = arr2[j]

    while len(ret) < len1 + len2:

        if arr1_val < arr2_val:
            ret.append(arr1_val)
            if i < len1 - 1:
                i += 1
                arr1_val = arr1[i]
            else:
                arr1_val = float('inf')

        elif arr1_val >= arr2_val:
            ret.append(arr2_val)
            if j < len2 - 1:
                j += 1
                arr2_val = arr2[j]
            else:
                arr2_val = float('inf')
    return ret

if __name__ == '__main__':
    a = [1, 3, 2, 4, 7, 6, 8, 5]
    print(merge_sort(a))

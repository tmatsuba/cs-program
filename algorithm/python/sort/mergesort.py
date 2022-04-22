def merge_sort(arr):
    if not arr:
        return arr

    start = 0
    end = len(arr) - 1

    return rec_merge_sort(arr, start, end)

def rec_merge_sort(arr, start, end):

    if len(arr) == 1:
        return arr

    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]

        return arr

    pivot = int(len(arr) / 2)
    return merge(rec_merge_sort(arr[:pivot], start, pivot - 1),
                 rec_merge_sort(arr[pivot:], pivot, end))

def merge(arr1, arr2):
    print(arr1, arr2)
    ret = list()
    len1 = len(arr1)
    len2 = len(arr2)

    i = j = 0
    arr1_val = arr1[i]
    arr2_val = arr2[j]

    while len(ret) < len1 + len2:
        print('arr1:', i, ':', arr1[i])
        print('arr2:', j, ':', arr2[j])

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
        print('condition:', len(ret) , ':',  len1, ':',  len2)

    return ret

if __name__ == '__main__':
    a = [1, 3, 2, 4, 7, 6, 8, 5]
    print(merge_sort(a))

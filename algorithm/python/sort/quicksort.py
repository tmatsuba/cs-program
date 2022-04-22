def quick_sort(arr:list):
    return _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr:list, start:int, end:int):
    if not arr:
        return arr

    pivot = arr[int((end + start) / 2)]
    i = start
    j = end
    while True:
        while arr[i] < pivot:
            i += 1
        while pivot < arr[j]:
            j -= 1
        if i >= j:
            break
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1
    if start < i - 1:
        _quick_sort(arr, start, i - 1)
    if j + 1 < end:
        _quick_sort(arr, j + 1, end)
    return arr

if __name__ == "__main__":
    print(quick_sort([1, 3, 2, 4, 7, 6, 8, 5]))

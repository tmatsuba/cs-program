def insert_sort(arr):
    for j in range(1, len(arr) ):

        temp = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > temp:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = temp
    return arr

if __name__ == "__main__":
    a = [1, 3, 2, 4, 7, 6, 8, 5]
    print(insert_sort(a))



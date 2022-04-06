def bubble_sort(arr):

    for i in range(0, len(arr) - 1):

        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
    return arr

if __name__ == "__main__":
    a = [1, 3, 2, 4, 7, 6, 8, 5]
    print(bubble_sort(a))

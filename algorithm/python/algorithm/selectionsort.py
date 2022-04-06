def selection_sort(arr):

    for left in range(0, len(arr)):

        positionOfMin = left

        for location in range(left + 1, len(arr)):
            if arr[location] < arr[positionOfMin]:
                positionOfMin = location

        temp = arr[left]
        arr[left] = arr[positionOfMin]
        arr[positionOfMin] = temp
    return arr

if __name__ == "__main__":
    a = [1, 3, 2, 4, 7, 6, 8, 5]
    print(selection_sort(a))


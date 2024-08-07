def find_min_index(arr) -> int:
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return arr[min_index], min_index


print(find_min_index([3, 4, 2, 9, 1, 10]))

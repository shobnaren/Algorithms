# Find the smallest item in the list
# move it to the first position
# repeat this process

def selection_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]


xs = [2, 5, 3, 1]
selection_sort(xs)
print(xs)
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))

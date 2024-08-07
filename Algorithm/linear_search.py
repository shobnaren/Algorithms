def linear_search(arr, target):
    for ind, val in enumerate(arr):
        if val == target:
            return ind
    return -1


print(linear_search([5, 3, 45, 67, 8], 67))

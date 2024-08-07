# method 1
def find_even(n):
    if n % 2 == 0:
        return n


arr = list(range(1, 101))
print(list(filter(find_even, arr)))

# method 2
arr2 = [i for i in range(1, 101) if i % 2 == 0]
print(arr2)

# use step parameter in range function
arr3 = [i for i in range(2,101,2)]
print(arr3)

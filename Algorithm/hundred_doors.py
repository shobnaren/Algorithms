def hundred_doors():
    door_state = {key: 1 for key in range(1, 101)}
    for i in range(2, 101):
        print('i iteration ', i)
        ind = i
        print('ind initial value', ind)

        while ind <= 100:
            print('j iteration:', ind)
            door_state[ind] = int(not door_state[ind])
            ind = ind + i
    print(door_state)
    open_doors = [k for k in range(1, 101) if door_state[k] == 1]
    print(open_doors)


def hundred_doors_array():
    doors = [True] * 101
    print(doors)
    for i in range(2, 101):
        for j in range(i, 101, i):
            doors[j] = not doors[j]

    open_dr = [val for val in range(1, 101) if doors[val] == True]
    print(open_dr)


hundred_doors()
hundred_doors_array()

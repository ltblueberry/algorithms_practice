def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        basis = arr[0]
        less = [i for i in arr[1:] if i <= basis]
        greater = [i for i in arr[1:] if i > basis]
        return quicksort(less) + [basis] + quicksort(greater)


my_list = [13, 44, 8, 26, 12, 2, 25, 11, 32, 4, 87, 54]

print quicksort(my_list)

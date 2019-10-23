def findSmallest(arr):
    smallest_index = 0
    smallest = arr[smallest_index]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def findBiggest(arr):
    biggest_index = 0
    biggest = arr[biggest_index]
    for i in range(1, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
    return biggest_index


def smallestSort(arr):
    newArr = []
    for _ in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def biggestSort(arr):
    newArr = []
    for _ in range(len(arr)):
        biggest = findBiggest(arr)
        newArr.append(arr.pop(biggest))
    return newArr


print smallestSort([13, 44, 8, 26, 12, 2, 25, 11, 32, 4, 87, 54])
print biggestSort([13, 44, 8, 26, 12, 2, 25, 11, 32, 4, 87, 54])

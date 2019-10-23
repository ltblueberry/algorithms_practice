import time


def dumb_search(list, item):
    for i in range(0, len(list)):
        if list[i] == item:
            return i
    return None


def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)/2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def checkTimeFor(title, additional, completion):
    start = time.time()
    result = completion(my_list, 44)
    end = time.time()
    print "{} = {}".format(title, result)
    print "{} = ".format(additional) + "%s seconds" % (end-start)


my_list = [1, 2, 4, 8, 11, 12, 13, 25, 26, 32, 44, 54, 87]

checkTimeFor("Binary search Index", "O(log2 n)", binary_search)
checkTimeFor("Dumb search Index", "O(n)", dumb_search)

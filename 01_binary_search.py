import time


def dump_search(list, item):
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


my_list = [1, 2, 4, 8, 11, 12, 13, 25, 26, 32, 44, 54, 87]

start1 = time.time()
result = binary_search(my_list, 44)
end1 = time.time()
print "Found index = {}".format(result)
print "O(log2 n) = " + "%s seconds" % (end1-start1)

start2 = time.time()
result = dump_search(my_list, 44)
end2 = time.time()
print "\nFound index = {}".format(result)
print "O(n) = " + "%s seconds" % (end2-start2)

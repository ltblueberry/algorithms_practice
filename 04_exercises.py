import time


def dumb_sum(arr):
    result = 0
    for item in arr:
        result += item
    return result


def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


def max(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    else:
        recursive = max(arr[1:])
        if arr[0] > recursive:
            return arr[0]
        else:
            return recursive


my_list = [13, 44, 8, 26, 12, 2, 25, 11, 32, 4, 87, 54]


def checkTimeFor(title, completion):
    start = time.time()
    result = completion(my_list)
    end = time.time()
    print "{} = {}".format(title, result)
    print "Time = " + "%s seconds" % (end-start)


checkTimeFor("Dumb sum", dumb_sum)
checkTimeFor("Sum", sum)
checkTimeFor("Max", max)

def recursion(i):
    if i > 10:
        return 10
    else:
        print(i)
        return recursion(i+1)


recursion(0)

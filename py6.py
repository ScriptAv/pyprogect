lis = [1, 2, 3]
tup = (1, 2, 3)

def squared(ar):
    ar = list(ar)
    ar = [a**2 for a in ar]
    return ar

def isType(ar):
    if type(ar) is list:
        ar = squared(ar)
        return ar
    elif type(ar) is tuple:
        ar = tuple(squared(ar))
        return ar
    else:
        return "it is not tuple or list"
print isType(lis)
print isType(tup)

s = [1, 2]
a = [3, 5]
def foo(s):
    s[0] = 3
    s[1] = 9
    return s
def fooo(s):
    """
        copy list
        ss = []
        ss.append(s[0])
        ss.append(s[1])
    """
    ss = s[:] #todo copy list
    ss[0] = 4
    ss[1] = 7
    return ss
print fooo(s)
print s
foo(s)
print s
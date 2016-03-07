s = [1, 2]
def foo(s):
    s[0] = 4
    s[1] = 7
    return s
foo(s)
print s
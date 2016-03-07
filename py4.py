# coding=utf-8
s = "sabrrtuwacaddabra"
s1 = sorted(s)
temp = list(set(s1))
s = sorted(temp)
print s
"""
    TODO
    di = {a: temp[a] for a in range(len(temp))}
"""
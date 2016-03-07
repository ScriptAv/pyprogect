a = "ambulance"
print a[-1: -len(a) - 1: -1] #1
a = list(a)#2
a.reverse()
a = ''.join(a)
print a


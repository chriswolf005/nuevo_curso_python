a=[1,2,3,5,]
b=a
print(a)
print(b)
del a [0]
print(id(b))
print(id(a))
c=a[:]
print(id(c))
a.append(6)
print(a)
print(b)
print(c)

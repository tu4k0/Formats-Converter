import copy

a = [1,2,3]
b = copy.deepcopy(a)
b.append(5)
print(a)
c=3
d = c
d += 5
print(id(c))
print(id(d))

print(1123 and 1234)

a = [1,2,3]
b = [1,2]

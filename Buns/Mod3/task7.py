elements = list(map(int, input().split(' ')))
a = any(elements.count(x) > 1 for x in elements)
print(a)

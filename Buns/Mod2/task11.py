elements = list(map(int, input().split(' ')))
a = False
for x in elements:
    if elements.count(x) > 1:
        a = True
print(a)

a = [x for x in input().split()]

set_a = set(a)

if len(set_a) == len(a):
    print("Все числа разные")
elif len(set_a) == 1:
    print("Все числа равны")
else:
    print("Есть равные и неравные числа")

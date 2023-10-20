def Quick_quadruple(base, level):
    if level == 0:
        return 1
    if level == 1:
        return base
    if level % 2 == 0:
        return Quick_quadruple(base**2,level/2)
    if level % 2 != 0:
        return base * Quick_quadruple(base,level-1)


base = int(input("Введите основание: "))
level = int(input("Введите степень: "))

print(Quick_quadruple(base, level))

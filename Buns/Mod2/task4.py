number = input()

try:
    number = int(number)
    if number < 0:
        raise ValueError
except ValueError:
    print(«Неверный ввод»)
    
else:
    print(bin(number)[2:])
    print(oct(number)[2:])
    print(hex(number)[2:])

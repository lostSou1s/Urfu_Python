def Evklid(num1,num2):
    if num1 == 0:
        return num2
    return Evklid(num2 % num1, num1)

print(Evklid(800,225))

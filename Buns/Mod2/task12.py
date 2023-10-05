phone_number = str(input())
chars = ['-', ')', '(', ' ']
for char in chars:
    phone_number = phone_number.replace(char, '')
print(phone_number)

phone_number = str(input())
for char in ['-', ')', '(', ' ']: phone_number = phone_number.replace(char, '')
print(phone_number)

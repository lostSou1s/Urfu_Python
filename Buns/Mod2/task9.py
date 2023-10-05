string = input()
vowels = "аеёиоуыэюя"
consonants = "бвгджзйклмнпрстфхцчшщ"
vowels_count = 0
consonants_count = 0
for char in string:
    if char in vowels:
        vowels_count += 1
    elif char in consonants:
        consonants_count += 1
print(vowels_count)
print(consonants_count)

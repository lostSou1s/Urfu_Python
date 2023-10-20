def char_count(word):
    count_char = {}
    for char in word:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    return count_char


def is_can_be_Palindrome(count_char):
    odd_count = 0
    for item in count_char.values():
        if item % 2 != 0:
            odd_count += 1
    return odd_count


def create_palindrome(count_char, odd_count):
    palindrome = ""
    key = ""
    for value in count_char.items():
        if value[1] % 2 == 0:
            palindrome += value[0] * (value[1] // 2)
        else:
            key = value[0]

    if odd_count == 1:
        return palindrome + key * count_char.get(key) + "".join(palindrome[::-1])

    return palindrome + "".join(palindrome[::-1])


word = input()

count_char = char_count(word)

odd_count = is_can_be_Palindrome(count_char)

if odd_count <= 1 and len(word) > 1:
    print(create_palindrome(count_char,odd_count))
else:
    print("не палиндром")

words = map(str, input().split(' '))
n_word = ""
for word in words:
    if len(word) > 0:
        n_word += word[-1]
print(n_word)

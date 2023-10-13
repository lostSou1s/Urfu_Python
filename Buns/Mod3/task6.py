words = input().split()
n_word = ''.join(word[-1] for word in words if len(word) > 0)
print(n_word)

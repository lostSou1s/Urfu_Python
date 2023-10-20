file = open("task5.txt")

all_words = []

for word in file:
    all_words.append(word)

char_count = {}

for word in all_words:
    for char in range(len(word)):
        if not (word[char].isalpha()): continue
        if word[char] in char_count:
            char_count[word[char]] += 1
        else:
            char_count[word[char]] = 1

char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
print(char_count)

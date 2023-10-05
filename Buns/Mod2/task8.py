def counter(string, char):
    count = 0
    for i in string:
        if i == char:
            count += 1   
        else:
            break
    return (count)
string_char = input()
string,char = string_char.split(",")
print(counter(string,char))


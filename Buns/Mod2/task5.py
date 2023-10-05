def shifter (char , n):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    index = chars.index(char)
    shift_char = (index + n) % len(chars) 
    shift = chars[shift_char]
    return shift
char_shift = input()
char,shift = char_shift.split(",")
print(shifter(char, int(shift)))

numbers = int(input())
copy_numbers = numbers
chet = 0
nechet = 0
while copy_numbers > 0:
    chet += copy_numbers % 10
    copy_numbers //= 100
while numbers > 0:
    numbers //= 10
    nechet += numbers % 10
    numbers //= 10
if chet + nechet * 3 == 90:
    print("yes")
else:
    print("no")

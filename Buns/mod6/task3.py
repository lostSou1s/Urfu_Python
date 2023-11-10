def get_armstrong_numbers():
    total = 10
    while True:
        number_array = [int(d) for d in str(total)]
        length_number = len(str(total))
        power_number = list(map(lambda x: x ** length_number, number_array))
        if sum(power_number) == total:
            yield total
        total += 1

cnt = 0

for i in get_armstrong_numbers():
    if cnt < 8:
        print(i, end=' ')
        cnt += 1
    else:
        break

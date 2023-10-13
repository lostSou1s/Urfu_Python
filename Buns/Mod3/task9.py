def get_loc(N):
    direct = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    current_dir = 0
    x, y = 0, 0

    for i in range(1, N+1):
        direction = direct[current_dir % 4]
        x += direction[0]
        y += direction[1]

        if (i % 2 == 0) and (i // 2 % 4 == 0 or i // 2 % 4 == 2):
            current_dir = (current_dir + 1) % 4

    return (x, y)

N = int(input())
print(get_loc(N))

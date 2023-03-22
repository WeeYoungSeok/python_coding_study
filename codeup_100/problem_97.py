h, w = map(int, input().split())

array = [[0 for col in range(w)] for row in range(h)]

n = int(input())

for _ in range(n):
    i, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(i):
            array[x - 1][y - 1] = 1
            y += 1
    else:
        for i in range(i):
            array[x - 1][y - 1] = 1
            x += 1

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end = " ")
    print()
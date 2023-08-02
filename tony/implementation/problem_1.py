# 달팽이
N = int(input())
K = int(input())
    
dal = [[0 for _ in range(N)] for _ in range(N)]

num = N**2
x = 0
y = 0

dx = 1
dy = 1

# 바퀴 수
t = N - 1


while t >= 2:
    for i in range(4):
        for j in range(t):
            dal[x][y] = num
            if i == 0:
                x += dx
            elif i == 1:
                y += dy
            elif i == 2:
                x -= dx
            elif i == 3:
                y -= dy
            num -= 1
    t -= 2
    x += 1
    y += 1

dal[x][y] = 1

result_x = 1
result_y = 1

for i in range(len(dal)):
    for j in range(len(dal[i])):
        if dal[i][j] == K:
            result_x += i
            result_y += j
        print(dal[i][j], end=" ")
    print()

print(result_x, result_y)
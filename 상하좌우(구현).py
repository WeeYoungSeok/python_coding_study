# 방향 벡터
# 동 북 서 남 기준
dx = [0, -1, 0, 1]
dy = [1, 0, -1 ,0]

# 구현 바트에서 좌표 (행렬) 이동 문제에서는 보통
# 방향 벡터를 이용한다.

# 행이 4개 열이 3개인 2차원 배열 초기화
# n = 4
# m = 3

# [[0] * m for _ in range(n)]

n = int(input())
data = input().split()

x = 1
y = 1

for vector in data:
    originX, originY = x, y
    if vector == 'R':
        x += dx[0]
        y += dy[0]
    elif vector == 'L':
        x += dx[2]
        y += dy[2]
    elif vector == 'U':
        x += dx[1]
        y += dy[1]
    else:
        x += dx[3]
        y += dy[3]
    if x < 1 or y < 1 or x > n or y > n:
        x = originX
        y = originY

print(x, y)

n = int(input())
data = input().split()

x, y = 1, 1

dx = [0, -1, 0, 1]
dy = [1, 0, -1 ,0]
move_types = ['R', 'U', 'L', 'D']

for move in data:
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)


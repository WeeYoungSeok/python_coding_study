# 배열돌리기1 pypy3로 제출
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for _ in range(r):
    # 시작 좌표
    x = 0
    y = 0

    # 끝 좌표
    max_x = n - 1
    max_y = m - 1
    for _ in range(min(n, m) // 2):
        if x > max_x or y > max_y:
            break
        nx = x
        ny = y
        temp = arr[nx][ny]

        # 세로 아래로
        for _ in range(max_x - x):
            if nx + 1 > max_x:
                break
            arr[nx + 1][ny], temp = temp, arr[nx + 1][ny]
            nx += 1

        # 가로 오른쪽으로
        for _ in range(max_y - y):
            arr[nx][ny + 1], temp = temp, arr[nx][ny + 1]
            ny += 1

        # 세로 위쪽으로
        for _ in range(max_x - x):
            arr[nx - 1][ny], temp = temp, arr[nx - 1][ny]
            nx -= 1

        # 가로 왼쪽으로
        for _ in range(max_y - y):
            arr[nx][ny - 1], temp = temp, arr[nx][ny - 1]
            ny -= 1

        x += 1
        y += 1
        max_x -= 1
        max_y -= 1


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
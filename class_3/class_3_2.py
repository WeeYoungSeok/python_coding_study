# 종이의 개수
import sys
input = sys.stdin.readline

def dfs(x, y, n):
    global minus_count, zero_count, plus_count
    num_check = papers[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if papers[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * (n // 3), y + l * (n // 3), n // 3)
                return
    if num_check ==  -1:
        minus_count += 1
    elif num_check == 0:
        zero_count += 1
    else:
        plus_count += 1

n = int(input())

papers = []

for _ in range(n):
    papers.append(list(map(int, input().split())))

minus_count = 0
plus_count = 0
zero_count = 0

dfs(0, 0, n)

print(str(minus_count) + "\n" + str(zero_count) + "\n" + str(plus_count))
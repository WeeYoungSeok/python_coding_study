# 유기농 배추

import sys   
# 백준에서는 재귀가 무제한으로 안되므로
# RecursionError가 발생한다.
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    if arr[x][y] == 1:
        arr[x][y] = -1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

t = int(input().strip())

for _ in range(t):
    m, n, k = map(int, input().strip().split())
    arr = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().strip().split())
        arr[y][x] = 1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)
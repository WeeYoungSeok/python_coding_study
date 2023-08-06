# 인구 이동
# baekjoon 16234
# https://www.acmicpc.net/problem/16234

import sys
from collections import deque
import math


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def input():
    return sys.stdin.readline()

n, l, r = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

result = 0

def bfs(x, y):
    de = deque()
    de.append((x, y))
    # 연합 국가 들
    union = [(x, y)]
    visited[x][y] = True
    # 연합 총 수 
    count = lst[x][y]
    while de:
        i, j = de.popleft()
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if l <= abs(lst[nx][ny] - lst[i][j]) and r >= abs(lst[nx][ny] - lst[i][j]):  
                # 인구차이 l명 이상, r명 이하인 경우, 연합 국가에 담기 
                union.append((nx, ny))
                visited[nx][ny] = True
                de.append((nx, ny))
                count += lst[nx][ny]

    for a, b in union:
        lst[a][b] = math.floor(count / len(union))
        
    return len(union)
            
    
while True:
    bool = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if visited[i][j] == False:
                if bfs(i, j) > 1:
                    bool = True
    if bool == False:
        break
    result += 1

print(result)
    
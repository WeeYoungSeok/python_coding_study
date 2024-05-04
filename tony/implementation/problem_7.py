# 기차가 어둠을 해치고
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 기차 만들기
sub = [[0 for _ in range(20)] for _ in range(n)]

for _ in range(m):
    com = list(map(int, input().split()))
    if com[0] == 1:
        sub[com[1] - 1][com[2] - 1] = 1
    elif com[0] == 2:
        sub[com[1] - 1][com[2] - 1] = 0
    elif com[0] == 3:
        sub[com[1] - 1] = [0] + sub[com[1] - 1][:len(sub[com[1] - 1]) - 1]
    else:
        sub[com[1] - 1] = sub[com[1] - 1][1:] + [0]

print(len(list(set(map(tuple, sub)))))
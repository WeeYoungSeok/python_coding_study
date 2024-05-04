# 원상복구(small)

n, k = map(int, input().split())

p = list(map(int, input().split()))

d = list(map(int, input().split()))

suffle = [0 for _ in range(n)]

for _ in range(k):
    for i in range(len(d)):
        suffle[d[i] - 1] = p[i]
    p = suffle.copy()

print(" ".join(map(str, p)))
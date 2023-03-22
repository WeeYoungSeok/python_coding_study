import math

m, n = map(int, input().split())

list = [True, True] + [False] * n

for i in range(2, int(math.sqrt(n)) + 1):
    for j in range(i + i, n + 1, i):
        if list[j] == False:
            list[j] = True

for i in range(m, n + 1):
    if list[i] == False:
        print(i)
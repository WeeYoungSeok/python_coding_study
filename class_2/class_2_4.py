import sys

input = sys.stdin.readline

n = int(input())

array = []
i = 0
for _ in range(n):
    inner = list(map(str, input().split()))
    inner.insert(1, i)
    inner[0] = int(inner[0])
    array.append(inner)
    i += 1
array.sort()

for i in array:
    print(i[0], i[2])
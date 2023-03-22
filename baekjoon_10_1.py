import sys

input = sys.stdin.readline

n, m = map(int, input().split())
max = 0
list = list(map(int, input().split()))

for i in range(len(list) - 2):
    for j in range(i + 1, len(list) - 1):
        for k in range(j + 1, len(list)):
            x = list[i] + list[j] + list[k]
            if x > m:
                continue
            if max < x:
                  max = x
print(max)
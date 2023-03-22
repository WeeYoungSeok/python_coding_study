# 분산 처리
import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    a, b = map(int, input().strip().split())
    if a % 10 == 0:
        print(10)
        continue
    b %= 4
    if b == 0:
        b = 4
    print(a ** b % 10)
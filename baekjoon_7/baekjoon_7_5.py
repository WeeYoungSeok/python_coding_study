import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    h, w, n = map(int, input().split())
    floor = n // h + 1
    n = n % h
    if n == 0:
        floor -= 1
        n = h
    print(n * 100 + floor)
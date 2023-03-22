import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque()

for _ in range(n):
    x = int(input())
    if x == 0:
        deq.pop()
    else:
        deq.append(x)

print(sum(deq))
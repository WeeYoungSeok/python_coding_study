import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

deq = deque()
count = 0

for _ in range(t):
    n, m = map(int, input().strip().split())
    x = deque(list(map(int, input().strip().split())))
    while len(x) != 0:
        max_value = max(x)
        pop = x.popleft()
        if pop >= max_value:
            count += 1
            m -= 1
            if m == -1:
                break
        else:
            x.append(pop)
            m -= 1
        if m < 0:
            m = len(x) - 1
    print(count)
    count = 0
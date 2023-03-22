import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
deq = deque()

for i in range(1, n + 1):
    deq.append(i)
  
if len(deq) == 1:
    print(deq[0])
else:
    while True:
        deq.popleft()
        if len(deq) == 1:
            print(deq[0])
            break
        deq.append(deq.popleft())
    
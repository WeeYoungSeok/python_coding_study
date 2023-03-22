# 최소 힙
import heapq, sys

input = sys.stdin.readline

n = int(input().strip())

heap = []

for _ in range(n):
    t = int(input().strip())
    if t == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, t)
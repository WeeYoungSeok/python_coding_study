# N번째 큰 수
import heapq
import sys

input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    nums = list(map(int, input().split()))
    if hq:
        for num in nums:
            min = hq[0]
            if num > min:
                heapq.heappop(hq)
                heapq.heappush(hq, num)
    else:
        for num in nums:
            heapq.heappush(hq, num)

print(hq[0])


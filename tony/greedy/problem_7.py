# 최소 회의실 개수

import sys, heapq

input = sys.stdin.readline

n = int(input())

meetings = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x:x[0])

heep = [meetings[0][1]]

for i in range(1, n):
    min_time = heapq.heappop(heep)
    heapq.heappush(heep, meetings[i][1])
    if min_time > meetings[i][0]:
        heapq.heappush(heep, min_time)

print(len(heep))
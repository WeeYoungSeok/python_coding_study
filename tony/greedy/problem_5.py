# 회의실 배정
import sys, heapq

input = sys.stdin.readline

n = int(input())

lecture_time = []

for _ in range(n):
    lecture_time.append(list(map(int, input().split())))

lecture_time.sort(key=lambda x:x[0])

rooms = [lecture_time[0][1]]

for i in range(1, n):
    min_time = heapq.heappop(rooms)
    heapq.heappush(rooms, lecture_time[i][1])
    if min_time > lecture_time[i][0]:
        heapq.heappush(rooms, min_time)


print(len(rooms))
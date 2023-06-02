# 회의실 배정
import sys

input = sys.stdin.readline

N = int(input())

n_array = []

for _ in range(N):
    n_array.append(list(map(int, input().split())))

n_array.sort(key = lambda x : (x[1], x[0]))

result = 1
end_time = n_array[0][1]
for i in range(1, N):
    if n_array[i][0] >= end_time:
        result += 1
        end_time = n_array[i][1]

print(result)
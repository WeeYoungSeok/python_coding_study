# 치킨 배달

import sys
import itertools

def input():
    return sys.stdin.readline()

n, m = map(int, input().split())

data = []
chicken = []
city = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 1:
            city.append([i, j])
        elif data[i][j] == 2:
            chicken.append([i, j])

chicken_comb = list(itertools.combinations(chicken, m))

result = 10000

for ch_cm in chicken_comb:
    city_dist = 0
    for c in city:
        dist = 10000
        for ch in ch_cm:
            dist = min(dist, abs(c[0] - ch[0]) + abs(c[1] - ch[1]))
        city_dist += dist
    result = min(result, city_dist)

print(result)
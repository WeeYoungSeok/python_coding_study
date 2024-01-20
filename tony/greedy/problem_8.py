# 백준 센서
# 진짜 문제 이거 이해 안된다
# 근데 행복 유치원하고 풀이 방식이 똑같은데
# 행복 유치원은 가장 큰 키 - 가장 작은 키라는 명시라도 되어있지 집중국이 뭔데 ㅠ

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int,input().split()))
sensor.sort()

array = []
for i in range(0,n-1):
    array.append(sensor[i+1] - sensor[i])

array.sort()

print(sum(array[:n-k]))
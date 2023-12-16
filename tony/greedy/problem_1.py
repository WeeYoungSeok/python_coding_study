# 에너지 드링크
import sys

input = sys.stdin.readline

n = int(input())

drinks = list(map(int, input().split()))

drinks.sort(reverse=True)
result = drinks[0]

for i in range(1, len(drinks)):
    result += drinks[i] / 2

if result.is_integer():
    print(int(result))
else:
    print(result)
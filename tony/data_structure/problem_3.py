# 문자열 집합
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

words = []
result = 0

for _ in range(n):
    words.append(input())

for _ in range(m):
    word = input()
    if word in words:
        result += 1

print(result)
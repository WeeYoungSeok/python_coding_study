# 파일 정리
import sys

input = sys.stdin.readline

n = int(input())

dic = {}

for _ in range(n):
    file = input().strip()
    extension = file.split(".")[1]
    if extension in dic:
        dic[extension] += 1
    else:
        dic[extension] = 1

dic = dict(sorted(dic.items()))

for key, value in dic.items():
    print(key, value)

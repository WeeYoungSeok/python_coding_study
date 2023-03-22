import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().strip().split()))

for i in range(len(array) - 1, -1, -1):
    print(array[i], end = " ")
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().strip().split()))

print(min(array))
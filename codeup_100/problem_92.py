import sys
input = sys.stdin.readline
numbers = [0] * 24

n = int(input())
array = list(map(int, input().strip().split()))

for i in array:
    numbers[i] += 1

for i in range(1, len(numbers)):
    print(numbers[i], end = " ")
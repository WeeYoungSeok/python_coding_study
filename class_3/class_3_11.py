import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

digit_list = list(map(int, input().strip().split()))

sum_list = [0]
total = 0

for i in range(len(digit_list)):
    total += digit_list[i]
    sum_list.append(total)

for _ in range(m):
    i, j = map(int, input().strip().split())
    print(sum_list[j] - sum_list[i - 1]) 
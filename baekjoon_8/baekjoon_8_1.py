import sys

input = sys.stdin.readline
n = int(input())

list = list(map(int, input().split()))

count = 0
bool = False

for i in list:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            bool = True
            break
    if bool == False:
        count += 1
    bool = False
print(count)    
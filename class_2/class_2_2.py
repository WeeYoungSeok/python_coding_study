import sys

input = sys.stdin.readline

n = int(input())

number_dict = {}
for _ in range(n):
    x = int(input())
    if number_dict.get(x) == None:
        number_dict[x] = 1
    else:
        number_dict[x] += 1

new_dict = sorted(number_dict.items())

for i in new_dict:
    for j in range(i[1]):
        print(i[0])
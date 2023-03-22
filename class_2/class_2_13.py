import sys

input = sys.stdin.readline

n = int(input().strip())
n_array = input().strip().split()
# n_array = set(input().split())

m = int(input().strip())
m_array = input().strip().split()

dict_n = {}

for i in n_array:
    if i in dict_n:
        dict_n[i] += 1
    else:
        dict_n[i] = 1

for i in m_array:
    if i in dict_n:
        print(dict_n[i])
    else:
        print("0")
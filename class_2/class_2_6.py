import sys

input = sys.stdin.readline

n, k = map(int, input().split())
array = [x for x in range(1, n + 1)]

remove = 0
remove_list = []
# while len(array) != 0:
#     for _ in range(k - 1):
#         if remove >= len(array):
#             remove = 0
#         remove += 1
#     if remove == len(array):
#         remove = 0
#     remove_list.append(str(array[remove]))
#     del array[remove]
for i in range(n):
    remove += (k - 1)
    if remove >= len(array):
        remove %= len(array)
    remove_list.append(str(array[remove]))
    array.pop(remove)

print("<", ", ".join(remove_list),">", sep = "")
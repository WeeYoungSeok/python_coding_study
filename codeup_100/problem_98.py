# array = [
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#   [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#   [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
#   [1, 0, 0, 0, 0, 1, 2, 1, 0, 1],
#   [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

array = []
for _ in range(10):
    lst = list(map(int, input().strip().split()))
    array.append(lst)
  
x = 1
y = 1
array[x][y] = 9

# 나의 풀이 시간 초과
# while True:
#     if array[x][y + 1] != 1:
#         if array[x][y + 1] == 2:
#             array[x][y + 1] = 9
#             break
#         else:
#             array[x][y + 1] = 9
#             y += 1
#     elif array[x + 1][y] != 1:
#         if array[x + 1][y] == 2:
#             array[x + 1][y] = 9
#             break
#         else:
#             array[x + 1][y] = 9
#             x += 1

while True:
    if array[x][y] == 0:
        array[x][y] = 9
    elif array[x][y] == 2:
        array[x][y] = 9
        break

    if array[x][y + 1] == 1 and array[x + 1][y] == 1:
        break

    if array[x][y + 1] == 1:
        x += 1
    elif array[x + 1][y] == 1:
        y += 1
    else:
        y += 1
          

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end = " ")
    print()
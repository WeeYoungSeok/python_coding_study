import sys
# import copy

input = sys.stdin.readline

n, m = map(int, input().split())

origin = []
count = []

for i in range(n):
    origin.append(input())

for a in range(n - 7):
    for b in range(m - 7):
        w_index = 0
        b_index = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                # 시작이 W일때랑 B일때랑 둘다 검사를 해야한다.
                # 처음과 같은 알파벳이어야한다.
                if (i + j) % 2 == 0:
                    if origin[i][j] != "W":
                        w_index += 1
                    if origin[i][j] != "B":
                        b_index += 1
                # 처음과 다른 알파벳이어야한다.
                else:
                    if origin[i][j] != "B":
                        w_index += 1
                    if origin[i][j] != "W":
                        b_index += 1
        count.append(min(w_index, b_index))
print(min(count))
        
# array = []

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def chessCheck(new_array):
#     # 현재 위치에서 상하좌우를 다 검사한다.
#     min_result = []
#     new_array2 = copy.deepcopy([row[y_start:y_end] for row in array[x_start : x_end]])
#     for x in range(2):  
#         result = 0
#         for i in range(len(new_array)):
#             for j in range(len(new_array[i])):
#                 # 0일때는 처음 칸이 B로 시작
#                 if x == 0:
#                     if i == 0 and j == 0:
#                         if new_array[i][j] != "B":
#                             new_array[i][j] = "B"
#                             result += 1
#                 else:
#                     if i == 0 and j == 0:
#                         if new_array[i][j] != "W":
#                             new_array[i][j] = "W"
#                             result += 1
#                 for k in range(4):
#                     n_x = i + dx[k]
#                     n_y = j + dy[k]
#                     if n_x >= len(new_array) or n_x <= -1 or n_y >= len(new_array[0]) or n_y <= -1:
#                         continue
#                     if new_array[n_x][n_y] == new_array[i][j]:
#                         if new_array[i][j] == "W":
#                             new_array[n_x][n_y] = "B"
#                         else:
#                             new_array[n_x][n_y] = "W"
#                         result += 1
#         min_result.append(result)
#         new_array = new_array2
#     return min(min_result)

# for _ in range(n):
#     inner = list(input().strip())
#     array.append(inner)

# check_array = []
# x_start = 0
# x_end = 8
# y_start = 0
# y_end = 8

# for _ in range((n - 7) * (m - 7)):
#     new_array = copy.deepcopy([row[y_start:y_end] for row in array[x_start : x_end]])
#     check_array.append(chessCheck(new_array))
#     y_start += 1
#     y_end += 1
#     if y_end > len(array[0]):
#         y_start = 0
#         y_end = 8
#         x_start += 1
#         x_end += 1
# print(min(check_array))

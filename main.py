# import sys

# input = sys.stdin.readline

# N = int(input())

# x_i = list(map(int, input().split()))

# x_i_sort = sorted(list(set(x_i)))

# # 여기서 그냥 배열끼리 비교해서
# # 하면 index 시간 복잡도가 O(n)이라서 n^2이 된다
# # 이 문제 n이 100만까지이므로 100만 X 100만이 되어버림
# # for i in x_i:
#     # print(x_i_sort.index(i), end=" ")

# # 튜플로 만들면 찾는 시간 복잡도가
# # O(1)이므로 시간이 많이 줄어든다.
# dic = {x_i_sort[i] : i for i in range(len(x_i_sort))}
# for i in x_i:
#     print(dic[i], end=" ")

# items = ['1', '2', '3', '4']
# from itertools import permutations
# print(list(permutations(items, 4)))

N = int(input())
K = int(input())
    
dal = [[0 for _ in range(N)] for _ in range(N)]

num = N**2
x = 0
y = 0

dx = 1
dy = 1

# 바퀴 수
t = N - 1


while t >= 2:
    for i in range(4):
        for j in range(t):
            dal[x][y] = num
            if i == 0:
                x += dx
            elif i == 1:
                y += dy
            elif i == 2:
                x -= dx
            elif i == 3:
                y -= dy
            num -= 1
    t -= 2
    x += 1
    y += 1

dal[x][y] = 1

result_x = 1
result_y = 1

for i in range(len(dal)):
    for j in range(len(dal[i])):
        if dal[i][j] == K:
            result_x += i
            result_y += j
        print(dal[i][j], end=" ")
    print()

print(result_x, result_y)


a, b, c = map(int, input().split())
print(a + b + c)
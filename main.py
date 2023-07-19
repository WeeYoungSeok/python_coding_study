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

n, k = map(int, input().split())

student_list = list(map(int, input().split()))

answer = 0

for i in range(0, int(n // k) + 1, k):
    answer += max(student_list[i:3]) - min(student_list[i:3])


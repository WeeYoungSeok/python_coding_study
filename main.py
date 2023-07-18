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

# 탑
import sys

input = sys.stdin.readline

n = int(input().strip("\n"))
    
answer = [0 for _ in range(0, n)]

razers = list(map(int, input().strip("\n").split()))
s = []

for i in range(0, len(razers)):
    if len(s) == 0:
        s.append([razers[i], i + 1])
        continue
    while len(s) > 0:
        pop_data = s.pop()
        if pop_data[0] > razers[i]:
            answer[i] = pop_data[1]
            s.append(pop_data)
            s.append([razers[i], i + 1])
            break
        else:
            if len(s) == 0:
                s.append([razers[i], i + 1])
                break

print(" ".join(map(str, answer)))
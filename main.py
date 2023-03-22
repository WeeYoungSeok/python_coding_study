# import random
# import sys
# from itertools import product

# input = sys.stdin.readline
# # 선택 정렬
# # 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]

# print(array)

# # 삽입 정렬
# # 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입합니다.
# # 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적입니다, (선택 정렬보다 빠름)

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j - 1]:
#             array[j], array[j - 1] = array[j - 1], array[j]
#         else:
#             break
# print(array)

# # 퀵 정렬
# # 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# # 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
# # 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
# # 가장 기본적인 퀵 정렬은 첫번째 데이터를 기준 데이터(pivot)로 설정

# # arr1 = ['빨강', '노랑']
# # arr2 = ['XL', 'L']
# # arr3 = ['a', 'b']
# # list = list(product(arr1, arr2, arr3))
# # print(list)

# a = "하 히"
# c1, c2 = a.split(" ")
# print(c1)
# print(c2)

# from collections import deque

# list = [1, 2, 5, 6]
# print(list.pop(0))

# def solution(n, k, cmd):
#     answer = ["O"] * n
#     table = {}
#     for i in range(n):
#         table[i] = [i - 1, i + 1]
#     table[0] = [None, 1]
#     table[n - 1] = [n - 2, None]
#     # 최근 삭제한 요소
#     stack = []
#     for word in cmd:
#         # 삭제
#         if word[0] == "C":
#             answer[k] = "X"
#             pre, next = table[k]
#             stack.append([pre, k, next])
#             # 커서 이동
#             # 마지막 번지를 삭제해주었다면 그 전의 커서로 가야한다.
#             if next == None:
#                 k = table[k][0]
#             # 마지막 번지 삭제가 아니라면?
#             else:
#                 k = table[k][1]

#             # 테이블 변환
#             # 가장 첫번째를 삭제 했다면
#             if pre == None:
#                 # 두번째의 항이 첫번째로 변해야하므로 두번째 항의 pre를 None로 바꾸어준다.
#                 table[next][0] = None
#             # 가장 마지막 번지를 삭제해주었다면
#             elif next == None:
#                 # 가장 마지막 번지 바로 위의 번지의 next는 None가 된다.
#                 table[pre][1] = None
#             else:
#                 table[pre][1] = next
#                 table[next][0] = pre
#         # 복구
#         elif word[0] == "Z":
#             pre, now, next = stack.pop()
#             answer[now] = "O"
#             # 복구된애의 전번지가 없는애라면
#             if pre == None:
#                 # 복구 후에는 복구된애의 다음것의 이전 포인터가 현재가 된다
#                 table[next][0] = now
#             # 복구된애의 다음번지가 없는애라면
#             elif next == None:
#                 # 복구 후에는 복구된애의 이전것의 다음 포인터가 현재가 된다
#                 table[pre][1] = now
#             else:
#                 # 그게 아니라면 복구 후에 중간에 낌으로서
#                 # 이전 번지의 다음 포인터는 현재가 되고
#                 # 다음 번지의 이전 포인터는 현재가 된다.
#                 table[pre][1] = now
#                 table[next][0] = now
#         # 커서 이동
#         else:
#             move_type, move_value = word.split(" ")
#             if move_type == "D":
#                 for _ in range(int(move_value)):
#                     # 커서를 현재 커서의 다음 커서로 바꾼다.
#                     k = table[k][1]
#             else:
#                 for _ in range(int(move_value)):
#                     # 커서를 현재 커서의 이전 커서로 바꾼다.
#                     k = table[k][0]
#     return "".join(answer)
# print(
#     solution(
#         8, 2,
#         ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))


# 나무 자르기
# n, m = map(int, input().split())
# trees = list(map(int, input().split()))

# result = 0
# start = 0
# end = max(trees)

# while start <= end:
#     mid = (start + end) // 2
#     count = 0
#     for tree in trees:
#         if tree > mid:
#             count += (tree - mid)
#     if count < m:
#         end = mid - 1
#     else:
#         start = mid + 1
#         result = mid

# print(result)

# 랜선 자르기
# n, m = map(int, input().split())

# lans = []
# for _ in range(n):
#     lans.append(int(input()))

# start = 0
# end = max(lans)
# result = 0

# while start <= end:
#     mid = (start + end) // 2
#     if mid == 0:
#         result = 1
#         break
#     count = 0
#     for lan in lans:
#         if lan >= mid:
#             count += (lan // mid)
#     if count < m:
#         end = mid - 1
#     else:
#         start = mid + 1
#         result = mid
# print(result)

# n, m, b = map(int, input().split())

# time = int(1e9)
# result = 0

# earth = []

# for _ in range(n):
#     earth.append(list(map(int, input().split())))

# for i in range(257):
#     use_block = 0
#     inven_block = 0
#     for j in range(n):
#         for k in range(m):
#             if earth[j][k] < i:
#                 use_block += (i - earth[j][k])
#             else:
#                 inven_block += (earth[j][k] - i)
#     # 사용된 블록이 인벤에 있는 블록보다 크다면 만들 수 없음
#     if use_block > b + inven_block:
#        continue
#     # 시간
#     count = (inven_block * 2) + use_block
#     # 시간이 같을 때 높이가 높은 순으로 나와야하므로 =을 붙여주어야한다.
#     if count <= time:
#         time = count
#         result = i
# print(time, result)

# def bubble_sort(arr):
#     bool = False
#     for i in range(len(arr)):
#         for j in range(len(arr) - 1, 0, -1):
#             if int(arr[j].split()[1]) > int(arr[j - 1].split()[1]):
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#                 bool = True
#     return bool

# def solution(K, user_scores):
#     answer = 0
#     rank = []
  
#     for i in range(len(user_scores)):
#         if len(rank) == 0:
#             rank.append(user_scores[i])
#             answer += 1
#         else:
#             user_name = user_scores[i].split()[0]
#             user_score = int(user_scores[i].split()[1])
#             bool = False
#             # 기존에 있던 랭크에서 내 이름과 같으면서 갱신 점수가 더 높다면 바꾸어준다.
#             for j in range(len(rank)):
#                 rank_name = rank[j].split()[0]
#                 rank_score = int(rank[j].split()[1])
#                 if rank_name == user_name:
#                     if rank_score < user_score:
#                         rank[j] = user_scores[i]
#                         bool = True
#                         break
#                     elif rank_score >= user_score:
#                         bool = True
#                         break
#             # 기존에 있던 랭크에 내 아이디가 없다면 새로운 사람이 들어온것이다.
#             insert_bool = False
#             if bool == False:
#                 check_bool = False
#                 for j in range(len(rank)):
#                     rank_name = rank[j].split()[0]
#                     rank_score = int(rank[j].split()[1])
#                     if user_score > rank_score:
#                         rank.insert(j, user_scores[i])
#                         check_bool = True
#                         answer += 1
#                         break     
#                 if check_bool == False:
#                     # 맨뒤에 삽입
#                     rank.append(user_scores[i])
#                     insert_bool = True
#             # 해당 행위가 완료되었다면
#             # 버블정렬 시행
#             # 버블 정렬 시행 후 자리가 바꼈다면
#             if bubble_sort(rank) == True:
#                 # 자리는 바꼈지만 배열이 더 크다면?
#                 if len(rank) > K:
#                     # 랭킹에 들어올수가 없다
#                     rank = rank[0:K]
#                 else:
#                     if insert_bool == True or bool == True:
#                         answer += 1
#             else:
#                 # 자리는 바꼈지만 배열이 더 크다면?
#                 if len(rank) > K:
#                     # 랭킹에 들어올수가 없다
#                     rank = rank[0:K]
#                 else:
#                     if insert_bool == True:
#                         answer += 1       
#     return answer

# print(solution(3, ["alex111 100", "cheries2 200", "coco 150", "luna 100", "alex111 120", "coco 300", "cheries2 110"]))
# print(solution(3, ["alex111 100", "cheries2 200", "alex111 200", "cheries2 150", "coco 50", "coco 200"]))
# print(solution(2, ["cheries2 200", "alex111 100", "coco 150", "puyo 120"]))

# from collections import deque

# def solution(N, coffee_times):
#     answer = []
#     if N == 1:
#         for i in range(len(coffee_times)):
#             answer.append(i + 1)
#     else:
        
#         coffee_times_dict_list = deque([])
      
#         for i in range(len(coffee_times)):
#             dict = {i : coffee_times[i]}
#             coffee_times_dict_list.append(dict)
          
#         order_dict = {}
#         while len(answer) != len(coffee_times):
#             if len(order_dict) < N:
#                 while coffee_times_dict_list:
#                     pop_coffee = coffee_times_dict_list.popleft()
#                     for key in pop_coffee:
#                         order_dict[key] = pop_coffee[key]
#                     if len(order_dict) == N:
#                         break
#             for key in list(order_dict.keys()):
#                 order_dict[key] -= 1
#                 if order_dict[key] == 0:
#                     answer.append(key + 1)
#                     del order_dict[key]
#     return answer

# print(solution(3, [4, 2, 2, 5, 3]))


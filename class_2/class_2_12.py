import sys


input = sys.stdin.readline

# 포함 여부는 set을 이용하면
# in 연산시 O(1)만큼 시간이 걸린다.
# 리스트는 in 연산시 O(N)만큼 시간이 걸린다.

n = int(input().strip())
# n_array = list(map(int, input().strip().split()))
n_array = set(input().split())

m = int(input().strip())
m_array = input().strip().split()

for i in m_array:
    if i in n_array:
        print("1")
    else:
        print("0")

# n_array.sort()
# bool = False
# for i in range(len(m_array)):
#     start = 0
#     end = len(n_array) - 1
#     while start <= end:
#         mid = int((start + end) / 2)
#         if n_array[mid] == m_array[i]:
#             print("1")
#             bool = True
#             break
#         elif n_array[mid] > m_array[i]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     if bool == False:
#         print("0")
#     bool = False
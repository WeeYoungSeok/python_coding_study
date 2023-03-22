import sys

input = sys.stdin.readline

n, m = map(int, input().split())

wood = list(map(int, input().strip().split()))

wood.sort()

# count = 0
# cut = wood[len(wood) // 2]
# for i in range(len(wood) // 2, len(wood)):
#     count += wood[i] - cut
  
result = 0
if len(wood) == 1 and wood[0] == m:
    print(wood[0] - m)
else:
    start = wood[0]
    end = wood[-1]
    while start <= end:
        mid = start + (end - start) // 2
        count = 0
      
        
    
  # for i in range(m - count):
  #     cut -= 1
  #     for j in range(len(wood)):
  #         if wood[j] - cut > 0:
  #             result += wood[j] - cut
  #     if result >= m:
  #         print(cut)
  #         break
  #     else:
  #         result = 0

# max_cut = 0
# count = 0
# for i in range(wood[-1]):
#     for j in range(len(wood)):
#         if count > m:
#             count = 0
#             break
#         if wood[j] - i > 0:
#             count += wood[j] - i
#         if count == m and j == len(wood) - 1:
#             if max_cut < i:
#                 max_cut = i
#     count = 0
# print(max_cut)
        
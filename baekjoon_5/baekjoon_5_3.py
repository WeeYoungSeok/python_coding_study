def hansu(num):
    result = 0
    temp = 0
    for i in range(1, num + 1):
        if i < 100:
            result += 1
            continue
        else:
            num_list = list(map(int, str(i)))
            temp = num_list[0] - num_list[1]
            for j in range(1, len(num_list)):
                if j + 1 == len(num_list):
                    result += 1
                    break
                sequence = num_list[j] - num_list[j + 1]
                if temp != sequence:
                    break
    return result
  
n = int(input())
print(hansu(n))
# result = 0

# for i in range(1, n + 1):
#     x = str(i)
#     temp = 0
#     if len(x) >= 3:
#         temp = int(x[0]) - int(x[1])
#     else:
#         result += 1
#         continue
#     for j in range(1, len(x)):
#         if j + 1 == len(x):
#             result += 1
#             break
#         sequence = int(x[j]) - int(x[j + 1])
#         if temp != sequence:
#             break
          
# print(result)

# 1000까지니깐 0번지 1번지 2번지로만 비교해서 가능
# def hansu(num):
#     result = 0
#     for i in range(1, num + 1):
#         num_list = list(map(int, str(i)))
#         if i < 100:
#             result += 1
#         else:
#             if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
#                 result += 1
#     return result
        
# n = int(input())

# print(hansu(n))

# import math

n = int(input())

# list = [False, False] + [True] * (n + 1)
# for i in range(2, int(math.sqrt(n)) + 1):
#     if list[i] == True:
#         for j in range(i + i, n + 1, i):
#             list[j] = False

# for i in range(2, len(list)):
#     if i == 0 or i == 1:
#         continue
#     if list[i] == True:
#         while True:
#             if n % i == 0:
#                 print(i)
#                 n //= i
#             else:
#                 break



i = 2
while n != 1:
    if n % i == 0:
        n /= i
        print(i)
    else:
        i += 1
    
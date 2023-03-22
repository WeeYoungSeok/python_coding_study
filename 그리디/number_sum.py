# n = int(input())
# result = 0
# count = 0
# i = 1
# while True:
#     result += i
#     i += 1
#     if result > n:
#         print(count)
#         break
#     elif result == n:
#         print(count + 1)
#         break
#     count += 1

s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)
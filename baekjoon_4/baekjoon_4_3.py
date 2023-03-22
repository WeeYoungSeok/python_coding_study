num = 1

for i in range(3):
    x = int(input())
    num *= x

for i in range(10):
    print(str(num).count(str(i)))


# num = 1

# for i in range(3):
#     x = int(input())
#     num *= x

# for i in range(10):
#     result = 0
#     for j in str(num):
#         if str(i) == j:
#             result += 1
#     print(result)
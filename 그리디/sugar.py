n = int(input())
result = 0

if n == 4 or n == 7:
    print("-1")
else:
    while True:
        if n % 5 == 0:
            print(result + (n // 5))
            break
        elif n % 5 == 3 and n % 3 == 0:
            print(result + (n // 5) + 1)
            break
        else:
            n -= 3
        result += 1
        if (n <= 0):
            print(result)
            break
        # elif n % 3 == 1:
        #     print(n // 3 - 1)
        #     break
        # else:
        #     print(n // 3)
        #     break

# n = int(input())

# if n == 4 or n == 7:
#     print("-1")
# else:
#     while True:
#         if n % 5 == 0:
#             print((n // 5))
#             break
#         elif n % 5 == 1 or n % 5 == 3:
#             print((n // 5) + 1)
#             break
#         elif n % 5 == 2 or n % 5 == 4:
#             print(n // 5 + 2)
#             break
# x, y = input().split()

# list_x = list(x)
# list_y = list(y)
# list_x.reverse()
# list_y.reverse()

# if int("".join(list_x)) > int("".join(list_y)):
#     print("".join(list_x))
# else:
#     print("".join(list_y))

a, b = map(str, input().split())
print("".join(reversed(a)))
# 전체 문자열 역순
# a : b : -1 a부터 b까지 역순으로
print(int(a[::-1]))
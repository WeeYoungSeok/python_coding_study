# x, y, z = map(int, input().split())

# if x == y == z:
#     print(10000 + (x * 1000))
# elif x == y of x == z:
#     print(1000  + (x * 100))
# elif y == z:
#     print(1000  + (y * 100))
# else:
#     print(max(x, y, z) * 100)

lst = sorted(list(map(int, input().split())))

if len(set(lst)) == 1:
    print(lst[0] * 1000 + 10000)
elif len(set(lst)) == 2:
    print(1000 + lst[1] * 100)
else:
    print(lst[2] * 100)
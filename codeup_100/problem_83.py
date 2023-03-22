r, g, b = map(int, input().split())

result = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            result += 1
print(result)

# print(r * g * b) result 선언 없이 이렇게 가능
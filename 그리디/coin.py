n, k = map(int, input().split())

array = []
for i in range(n):
    a = int(input())
    array.append(a)
array.sort(reverse = True)
result = 0
for i in array:
    if k - i < 0:
        continue
    else:
        result += k // i
        k %= i

print(result)
n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)
result = 0
for i in range(len(a)):
    result += a[i] * b[i]
print(result)

# bMax = 0
# aMin = 0

# result = 0
# while len(a) > 0:
#     aMin = min(a)
#     bMax = max(b)
#     result += aMin * bMax
#     a.remove(aMin)
#     b.remove(bMax)
# print(result)


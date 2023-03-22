n = int(input())

array = list(map(int, input().split()))

array.sort()
result = 0
minute = 0
for i in array:
    result += i + minute
    minute += i

print(result)
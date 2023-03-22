a, d, n = map(int, input().split())

result = a

for _ in range(n - 1):
    result += d
print(result)
a, m, d, n = map(int, input().split())

result = a

for _ in range(n - 1):
    result *= m
    result += d
print(result)
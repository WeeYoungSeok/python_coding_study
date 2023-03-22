t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    zero = [x for x in range(1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            zero[j] += zero[j - 1]
    print(zero[-1])

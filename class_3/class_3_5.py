# 1로 만들기
x = int(input())

answer = 0

dp = [0] * 1000001

dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(4, x + 1):
    if i % 3 == 0 and i % 2 != 0:
        dp[i] = min(dp[i - 1], dp[i // 3]) + 1
    elif i % 3 != 0 and i % 2 == 0:
        dp[i] = min(dp[i - 1], dp[i // 2]) + 1
    elif i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i - 1], dp[i // 2], dp[i // 3]) + 1
    else:
        dp[i] = dp[i - 1] + 1
print(dp[x])

# 다른 풀이
n = int(input())
d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)	
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
print(d[n])
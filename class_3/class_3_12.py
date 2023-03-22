# dp pypy로만 통과가능

n = int(input())

dp = [0] * (n + 1)
# 제곱근 갯수를 먼저 저장 무조건 1개
k = 1
while k**2 <= n:
    dp[k**2] = 1
    k += 1
    
for i in range(1, n + 1):
    if dp[i] != 0:
        continue
    j = 1
    while j*j <= i:
        if dp[i] == 0:
            dp[i] = dp[j*j] + dp[i - j*j]
        else:
            dp[i] = min(dp[i], dp[j*j] + dp[i - j*j])
        j += 1

print(dp[n])
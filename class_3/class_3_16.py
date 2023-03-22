# 계단 오르기
# https://sundries-in-myidea.tistory.com/22
# 설명 진짜 깔끔하다.

n = int(input())

l = [0] * 301
dp = [0] * 301

for i in range(n):
    l[i] = int(input())

dp[0] = l[0]
dp[1] = l[0] + l[1]
dp[2] = max(l[0] + l[2], l[1] + l[2])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + l[i - 1] + l[i], dp[i - 2] + l[i])

print(dp[n - 1])
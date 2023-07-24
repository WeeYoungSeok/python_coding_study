# 동전 2
n, k = map(int, input().split())

coins = []
for _ in range(0, n):
    coins.append(int(input()))
coins.sort()

dp = [10001] * (k + 1)

for i in range(1, k + 1):
    if coins[0] > i:
        continue
    else:
        for j in range(0, len(coins)):
            if i % coins[j] == 0:
                dp[i] = i // coins[j]
            if i - coins[j] >= 0:
                if dp[i - coins[j]] != 10001:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])


# 다른 풀이
# 동전을 돌면서 dp를 검사하기..
n, k = map(int, input().split())

coins = []
for _ in range(0, n):
    coins.append(int(input()))
coins.sort()

dp = [10001] * (k + 1)
# 동전으로 만들 수 있는 최소의 값을 만들어주기 위함
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
        
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
# 피보나치 수
fibo = [0, 1, 1]

n = int(input())

for i in range(3, n + 1):
    fibo.append((fibo[i - 2] + fibo[i - 1]))

print(fibo[-1])
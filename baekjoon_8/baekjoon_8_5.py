list = [0, 0] + [1] * (123456 * 2 - 1)
for i in range(2, int(len(list) ** 0.5) + 1):
    if list[i] == 1:
        for j in range(i + i, len(list), i):
            list[j] = 0
          
while True:
    n = int(input())
    if n == 0:
        break
    print(sum(list[n + 1:(n * 2) + 1]))
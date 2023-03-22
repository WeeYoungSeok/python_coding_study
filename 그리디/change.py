n = int(input())

change = 1000 - n
coin = [500, 100, 50, 10, 5, 1]
result = 0

for i in coin:
    if change // i > 0:
        result += change // i
        change %= i

print(result)
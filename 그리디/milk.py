n = int(input())

milk = list(map(int, input().split()))

milk_type = 0

result = 0

for i in milk:
    if i == milk_type:
        result += 1
        milk_type += 1
    if milk_type > 2:
        milk_type = 0
print(result)
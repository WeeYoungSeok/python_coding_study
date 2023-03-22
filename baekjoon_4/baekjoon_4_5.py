n = int(input())

score = list(map(int, input().split()))

max = max(score)

result = 0

for i in score:
    result += i / max * 100

print(result/ len(score))
        
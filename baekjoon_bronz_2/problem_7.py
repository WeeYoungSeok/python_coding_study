# 이상한 곱셈
a, b = input().split()

answer = 0

before_num = 0
for i in a:
    before_num += int(i)
for i in b:
    answer += (before_num * int(i))

print(answer)

# 그냥 더해서 곱해도 됨
a, b = map(int, input())
a, b = list(map(int, a)), list(map(int, b))

print(sum(a) * sum(b))
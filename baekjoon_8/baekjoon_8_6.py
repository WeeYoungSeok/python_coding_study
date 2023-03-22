# 소수 구하기
# 0은 False, 1은 True로 판별해도됨
# 갯수 구할땐 sum을 써도됨
list = [0, 0] + [1] * (10000 * 2 - 1)
for i in range(2, int(len(list) ** 0.5) + 1):
    if list[i] == 1:
        for j in range(i + i, len(list), i):
            list[j] = 0

n = int(input())
for _ in range(n):
    x = int(input())
    other_list = []
    for i in range(2, x):
        if list[i] == 1:
            if list[x - i] == 1:
                other_list.append([i, x - i])
    if len(other_list) < 2:
        print(other_list[0][0], other_list[0][1])
    else:
        min, k = 10000, 0
        for h in range(len(other_list)):
            if abs(other_list[h][0] - other_list[h][1]) < min:
                min = abs(other_list[h][0] - other_list[h][1])
                k = h
        print(other_list[k][0], other_list[k][1])
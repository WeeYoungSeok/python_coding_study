# 소수 구하기
# 0은 False, 1은 True로 판별해도됨
# 갯수 구할땐 sum을 써도됨
list = [0, 0] + [1] * (123456 * 2 - 1)
for i in range(2, int(len(list) ** 0.5) + 1):
    if list[i] == 1:
        for j in range(i + i, len(list), i):
            list[j] = 0
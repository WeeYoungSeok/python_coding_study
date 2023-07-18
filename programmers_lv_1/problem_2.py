# 부족한 금액 계산하기
def solution(price, money, count):
    for i in range(0, count):
        money -= (i + 1) * price
    return 0 if money >= 0 else -money
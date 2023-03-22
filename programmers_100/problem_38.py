# 약수 구하기
def solution(n):
    return [i for i in range(1, n + 1) if n % i == 0]
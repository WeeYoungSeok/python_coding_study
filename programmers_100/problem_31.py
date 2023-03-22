# 제곱수 판별하기
import math

def solution(n):
    if math.sqrt(n) != int(math.sqrt(n)):
        return 2
    return 1

def solution2(n):
    return 1 if (n ** 0.5).is_integer else 2
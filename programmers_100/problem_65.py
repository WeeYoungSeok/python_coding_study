# 팩토리얼
def solution(n):
    answer = 0
    for i in range(1, 11):
        result = 1
        for j in range(1, i + 1):
            result *= j
        if result > n:
            return answer
        answer = i
    return answer

# math의 factorial 이용
from math import factorial
def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
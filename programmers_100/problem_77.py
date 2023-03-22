# 구슬을 나누는 경우의 수
import math
def solution(balls, share):
    return math.factorial(balls) // (math.factorial(balls - share) * math.factorial(share))

# 조합 라이브러리
def solution(balls, share):
    return math.comb(balls, share)
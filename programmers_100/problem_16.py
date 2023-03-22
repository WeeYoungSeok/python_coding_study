# 피자 나눠 먹기(1)
def solution(n):
    # 나머지
    mod = n % 7
    if mod > 0:
        return (n // 7) + 1
    return n // 7

# 피자 나눠 먹기(1) 다른 사람 풀이
def solution2(n):
    return (n - 1) // 7 + 1
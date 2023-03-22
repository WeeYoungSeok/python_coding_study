# 양꼬치
def solution(n, k):
    answer = 0
    answer += (12000 * n)
    k = k - (n // 10)
    if k > 0:
        answer += (k * 2000)
    return answer
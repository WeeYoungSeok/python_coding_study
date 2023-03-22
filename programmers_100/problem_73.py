# 종이 자르기
def solution(M, N):
    answer = 0
    for _ in range(M - 1):
        answer += 1
    for _ in range(N - 1):
        answer += M
    return answer

# 수학 공식
def solution(M, N):
    return (M * N) - 1
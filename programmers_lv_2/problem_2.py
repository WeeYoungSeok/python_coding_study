# 점프와 순간이동

def solution(n):
    # 처음에는 무조건 뛰어야하므로 건전지 사용랑 1듬
    answer = 1
    while n != 1:
        # 짝수라면 이동 없이 순간이동 가능
        if n % 2 == 0:
            n /= 2
        # 홀수라면 1칸 이동
        else:
            answer += 1
            n -= 1
    return answer
# 소인수분해
def solution(n):
    answer = set()
    for i in range(2, n + 1):
        while n != 1:
            if n % i != 0:
                break
            n //= i
            answer.add(i)
    return sorted(answer)
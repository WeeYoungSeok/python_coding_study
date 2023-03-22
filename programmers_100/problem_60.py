# 합성수 찾기
def solution(n):
    answer = 0
    for i in range(4, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count >= 3:
            answer += 1
    return answer

# 다른 사람 풀이
# 1 ~ 3은 합성수가 절대 될 수 없으므로
# 4부터 돈다
# inner loop은 2부터 루트 자기 자신 + 1까지 도는 이유는
# 루트를 씌우고 +1 이상인 수는 자기 자신의 약수가 절대 될 수 없으므로
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output
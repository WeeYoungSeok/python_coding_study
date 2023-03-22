# 연속된 수의 합
def solution(num, total):
    answer = []
    for i in range(-1000, 1001):
        check_num = 0
        for j in range(i, i + num):
            check_num += j
        if check_num == total:
            for j in range(i, i + num):
                answer.append(j)
            return answer
    return answer
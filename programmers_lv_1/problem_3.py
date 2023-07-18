# 삼총사
def solution(number):
    answer = 0
    i = 0
    while i < len(number) and len(number) - i > 2:
        zero = number[i]
        for j in range(i + 1, len(number)):
            zero += number[j]
            for k in range(j + 1, len(number)):
                if zero + number[k] == 0:
                    answer += 1
            zero = number[i]
        i += 1
    return answer
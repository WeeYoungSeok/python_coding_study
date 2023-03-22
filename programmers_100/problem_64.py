# 2차원으로 만들기
def solution(num_list, n):
    answer = []
    inner = []
    for i in range(len(num_list)):
        inner.append(num_list[i])
        if (i + 1) % n == 0:
            answer.append(inner)
            inner = []
    return answer

# slice 이용
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i + n])
    return answer
# 7의 개수
def solution(array):
    answer = 0
    for word in array:
        answer += str(word).count("7")
    return answer
# k의 개수
def solution(i, j, k):
    answer = 0
    for word in range(i, j + 1):
        answer += str(word).count(str(k))
    return answer
# 가자 큰 수 찾기
def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer
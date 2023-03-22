# 가까운 수
def solution(array, n):
    answer = array[0]
    array.sort()
    min_value = abs(n - array[0])
    for i in range(1, len(array)):
        if min_value > abs(n - array[i]):
            min_value = abs(n - array[i])
            answer = array[i]
        else:
            break
    return answer
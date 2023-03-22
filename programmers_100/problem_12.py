# 중복된 숫자 개수
def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer

# 중복된 숫자 개수 2
def solution2(array, n):
    return array.count(n)
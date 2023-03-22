# 중앙값 구하기
def solution(array):
    array.sort()
    return array[len(array) // 2 - 1] if len(array) % 2 == 0 else array[len(array) // 2]

# 다른 풀이 
def solution2(array):
    array.sort()
    return array[len(array) // 2]

# 중앙값이 배열의 길이가 짝수일 경우 중앙값은 len(array) // 2 거나 len(array) // 2 - 1 인듯하다. 둘다 정답 처리
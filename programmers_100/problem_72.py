# 공 던지기
def solution(numbers, k):
    idx = 0
    for _ in range(k - 1):
        idx += 2
        if idx >= len(numbers):
            idx -= len(numbers)
    return numbers[idx]
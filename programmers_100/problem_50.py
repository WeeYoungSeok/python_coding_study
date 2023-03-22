# 배열 회전시키기
# 내 풀이 심각함
def solution(numbers, direction):
    answer = [i for i in numbers]
    if direction == "right":
        for i in range(len(numbers)):
            if i == len(numbers) - 1:
                answer[0] = numbers[i]
            else:
                answer[i + 1] = numbers[i]
    else:
        for i in range(len(numbers)):
            if i == 0:
                answer[len(answer) - 1] = numbers[i]
            else:
                answer[i - 1] = numbers[i]
    return answer

# 리스트 더하기
def solution1(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[0 : len(numbers) - 1]
    else:
        return numbers[1 : len(numbers)] + [numbers[0]]

# queue
from collections import deque
def solution2(numbers, direction):
    queue = deque(numbers)
    if direction == "right":
        # 1번 오른쪽으로 회전
        queue.rotate(1)
    else:
        queue.rotate(-1)
    return list(queue)

# slice 이용
def solution3(numbers, direction):
    if direction == "right":
        return numbers[-1:] + numbers[:-1]
    else:
        return numbers[1:] + numbers[:1]
    
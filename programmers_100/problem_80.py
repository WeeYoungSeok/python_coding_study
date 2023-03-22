# 문자열 밀기
# 순수 코딩
def solution(A, B):
    for i in range(len(A)):
        if A[-i:] + A[:-i] == B:
            return i
    return -1

# queue 이용
from collections import deque
def solution(A, B):
    a, b = deque(A), deque(B)
    for i in range(len(A)):
        if a == b:
            return i
        a.rotate(1)
    return -1
# ZOAC

# 내풀이는 조합으로 했다
# 메모리 초과로 인해 코드를 보았다..
# 이런건 진짜 생각하기 힘들거같다
# 조금 더 고민해봐야겠다 ㅠ

# 해답 풀이
import sys

input = sys.stdin.readline

s = list(input().strip())

result = [""] * len(s)


def solution(arr, start):
    if not arr:
        return
    min_word = min(arr)
    min_word_idx = arr.index(min_word)
    result[start + min_word_idx] = min_word
    print("".join(result))
    solution(arr[min_word_idx + 1:], start + min_word_idx + 1)
    solution(arr[:min_word_idx], start)


solution(s, 0)

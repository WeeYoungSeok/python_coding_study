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

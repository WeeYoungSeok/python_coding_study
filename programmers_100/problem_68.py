# 한 번만 등장한 문자
def solution(s):
    answer = ''
    for word in s:
        if s.count(word) == 1:
            answer += word
    return "".join(sorted(answer))
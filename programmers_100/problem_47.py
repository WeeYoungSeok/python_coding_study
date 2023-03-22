# 대문자와 소문자
def solution(my_string):
    answer = ''
    for word in my_string:
        if word.isupper():
            answer += word.lower()
        else:
            answer += word.upper()
    return answer
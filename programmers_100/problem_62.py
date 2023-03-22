# 중복된 문자 제거
def solution(my_string):
    answer = []
    for word in my_string:
        if word not in answer:
            answer.append(word)
    return "".join(answer)

# 중복된 문자 제거2
def solution1(my_string):
    answer = ''
    for word in my_string:
        if word not in answer:
            answer += word
    return answer
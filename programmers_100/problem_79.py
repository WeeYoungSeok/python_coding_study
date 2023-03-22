# 문자열 계산하기
def solution(my_string):
    return eval(my_string)

# 와우
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
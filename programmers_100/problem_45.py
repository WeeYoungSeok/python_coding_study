# 문자열 정렬하기(1)
def solution(my_string):
    answer = sorted(my_string)
    answer = [int(i) for i in answer if i.isdigit()]
    return answer

# 한줄로
def solution2(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])
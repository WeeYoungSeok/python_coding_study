# 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    answer = 0
    for i in my_string:
        if not i.isalpha():
            answer += int(i)
    return answer

# 함수 이용
def solution2(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
# 숨어있는 숫자의 덧셈(2)
def solution(my_string):
    digit_list = []
    digit_value = "0"
    for word in my_string:
        if word.isdigit():
            digit_value += word
        else:
            digit_list.append(int(digit_value))
            digit_value = "0"
    digit_list.append(int(digit_value))
    return sum(digit_list)
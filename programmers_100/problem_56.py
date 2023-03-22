# 인덱스 바꾸기
def solution(my_string, num1, num2):
    my_string_list = list(my_string)
    my_string_list[num1] = my_string[num2]
    my_string_list[num2] = my_string[num1]
    return "".join(my_string_list)

# 콤마로 바꾸기 (콤마로 바꿀시에는 리스트가 바뀌지 않고 한번에 바뀜)
def solution1(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return "".join(my_string)
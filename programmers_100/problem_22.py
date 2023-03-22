# 문자열 뒤집기
def solution(my_string):
    str_list = list(my_string)
    str_list.reverse()
    return "".join(str_list)

# 문자열 뒤집기 2
def solution2(my_string):
    # 전체 리스트를 거꾸로 출력
    # 문자열에서도 이용가능
    return my_string[::-1]
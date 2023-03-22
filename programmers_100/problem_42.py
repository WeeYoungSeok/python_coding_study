# 모음 제거
def solution(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    for i in vowels:
        if i in my_string:
            my_string = my_string.replace(i, "")
    return my_string
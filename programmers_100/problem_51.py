# 외계행성의 나이
def solution(age):
    answer = ''
    age_dict = {"0" : "a", "1" : "b", "2" : "c", "3" : "d", "4": "e", "5" : "f", "6" : "g", "7" : "h", "8" : "i", "9" : "j"}
    for i in str(age):
        answer += age_dict[i]
    return answer

# 아스키코드 이용
def solution1(age):
    answer = ''
    for word in str(age):
        answer += chr(int(word) + 97)
    return answer

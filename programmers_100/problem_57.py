# 암호 해독
def solution(cipher, code):
    answer = ''
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]
    return answer

# 한줄로 표현
def solution1(cipher, code):
    return cipher[code -1::code]
# 가위 바위 보
def solution(rsp):
    answer = ''
    for word in rsp:
        if word == "2":
            answer += "0"
        elif word == "0":
            answer += "5"
        else:
            answer += "2"
    return answer

# 깔끔 풀이
def solution2(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
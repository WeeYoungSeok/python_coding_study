# 최빈값 구하기
def solution(array):
    answer = 0
    dict = {}
    for i in array:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    if len(dict) == 1:
        return dict[0][0]
    if dict[0][1] == dict[1][1]:
        return -1
    return dict[0][0]
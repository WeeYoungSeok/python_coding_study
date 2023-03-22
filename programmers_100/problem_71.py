# 진료 순서 정하기
def solution(emergency):
    answer = [0] * len(emergency)
    new_list = emergency.copy()
    new_list.sort(reverse = True)
    for i in range(len(new_list)):
        answer[emergency.index(new_list[i])] = i + 1
    return answer

# 코드 간결화
def solution(emergency):
    e = sorted(emergency, reverse = True)
    return [e.index(i) + 1 for i in emergency]

# 한줄 표현
def solution(emergency):
    return [sorted(emergency, reverse = True).index(e) for e in emergency]
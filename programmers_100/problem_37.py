# 개미 군단
def solution(hp):
    answer = 0
    while hp != 0:
        if hp // 5 > 0:
            answer += (hp // 5)
            hp %= 5
        elif hp // 3 > 0:
            answer += (hp // 3)
            hp %= 3
        else:
            answer += hp
            hp = 0
    return answer

# 다른 사람 풀이
def solution2(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
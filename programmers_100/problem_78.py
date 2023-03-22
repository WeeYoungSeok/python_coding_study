# 외계어 사전
def solution(spell, dic):
    for word in dic:
        bool = True
        for s in spell:
            if s not in word:
                bool = False
                break
        if bool == True:
            return 1
    return 2

# 리스트 비교로 푼 문제
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
        return 2

# 집합
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
# 다음에 올 숫자
def solution(common):
    # 등차
    if common[0] - common[1] == common[1] - common[2]:
        return common[-1] + common[1] - common[0]
    # 등비
    return common[-1] * (common[1] // common[0])
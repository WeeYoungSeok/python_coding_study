# 평행
# 기울기 = y값의 변화량 / x값의 변화량
def solution(dots):
    answer = 0
    lean_arr = []
    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            cur_lean = (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0])
            if cur_lean in lean_arr:
                return 1
            else:
                lean_arr.append(cur_lean)
    return answer
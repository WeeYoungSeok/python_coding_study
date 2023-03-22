# 다항식 더하기
def solution(polynomial):
    sum_x = 0
    sum_num = 0
    for word in polynomial.split(" + "):
        if "x" in word:
            if len(word) > 1:
                sum_x += int(word[:-1])
            else:
                sum_x += 1
        else:
            sum_num += int(word)
    if sum_x > 0 and sum_num == 0:
        if sum_x == 1:
            return "x"
        return str(sum_x) + "x"
    elif sum_x == 0 and sum_num > 0:
        return str(sum_num)
    else:
        if sum_x == 1:
            return "x + " + str(sum_num)
        return str(sum_x) + "x + " + str(sum_num)
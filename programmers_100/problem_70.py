# 이진수 더하기
# 순수 계산법
def solution(bin1, bin2):
    answer = ''
    bin1 = list(bin1[-1::-1])
    bin2 = list(bin2[-1::-1])
    sum_value = 0
    # 2진수의 합
    for i in range(len(bin1)):
        if bin1[i] == "1":
            sum_value += (2 ** i)
    for i in range(len(bin2)):
        if bin2[i] == "1":
            sum_value += (2 ** i)

    if sum_value == 0:
        return "0"
    # 10진수 -> 2진수
    while sum_value != 1:
        if sum_value % 2 == 0:
            answer += "0"
        else:
            answer += "1"
        sum_value //= 2
    answer += "1"
    return "".join(answer[-1::-1])

# 파이썬 라이브러리로 풀기
def solution(bin1, bin2):
   return bin(int(bin1, 2) + int(bin2, 2))[2:]
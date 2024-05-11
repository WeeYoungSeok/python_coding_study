# 홀수 홀리 호석
import sys

input = sys.stdin.readline


# 홀수의 갯수 구하기
def odd_count(num):
    add_odd_total = 0
    while num != 0:
        if (num % 10) % 2 != 0:
            add_odd_total += 1
        num //= 10
    return add_odd_total


def solution(num, odd_total):
    if len(num) == 1:
        odd_totals.append(odd_total)
        return
    elif len(num) == 2:
        new_num = int(num[0]) + int(num[1])
        solution(str(new_num), odd_total + odd_count(new_num))
    else:
        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                new_num = int(num[:i]) + int(num[i:j]) + int(num[j:])
                solution(str(new_num), odd_total + odd_count(new_num))


num = int(input())
odd_totals = []
solution(str(num), odd_count(num))
print(min(odd_totals), max(odd_totals))
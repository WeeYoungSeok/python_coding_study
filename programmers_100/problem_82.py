# 유한소수 판별하기
import math


def solution(a, b):
    gcd = math.gcd(a, b)
    a //= gcd
    b //= gcd
    check_set = set([2, 5])
    b_set = set()
    while b != 1:
        if b % 2 == 0:
            b_set.add(2)
            b //= 2
            continue
        elif b % 5 == 0:
            b_set.add(5)
            b //= 5
            continue
        else:
            b_set.add(b)
            break
    if not b_set - check_set:
        return 1
    return 2


# 굳이 set 비교 없이 b가 소인수분해 2와 5로만 했을 때 1이 되면 유한소수
def solution(a, b):
    b //= gcd(a, b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    return 1 if b == 1 else 2

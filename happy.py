# 콤마를 알아내기 위해서는
# 열 // 숫자 = x좌표
# 열 % 숫자 = y좌표
# 단 2차원 배열이 0부터 1씩 증가함에 따라 적용

import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())

print(x // m, x % m)
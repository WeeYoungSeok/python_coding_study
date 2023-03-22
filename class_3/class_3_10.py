# 나는야 포켓몬 마스터 이다솜
# 나의 풀이
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

poket_digit = {}
poket_alpha = {}

for i in range(n):
    poket = input().strip()
    poket_digit[i] = poket
    poket_alpha[poket] = i
    

for _ in range(m):
    dogam = input().strip()
    if dogam.isdigit():
        print(poket_digit[int(dogam) - 1])
    else:
        print(poket_alpha[dogam] + 1)

# dict를 하나로
input = sys.stdin.readline

n, m = map(int, input().split())

poket_dict = {}

for i in range(n):
    poket = input().strip()
    poket_dict[i] = poket
    poket_dict[poket] = i
    

for _ in range(m):
    dogam = input().strip()
    if dogam.isdigit():
        print(poket_dict[int(dogam) - 1])
    else:
        print(poket_dict[dogam] + 1)
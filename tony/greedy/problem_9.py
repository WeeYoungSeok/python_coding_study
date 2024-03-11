# 내 풀이
import sys

input = sys.stdin.readline

n = int(input())
print(n // 5)
print(n / 5)

if n < 5:
    if n == 1 or n == 3:
        print(-1)
    elif n == 2 or n == 4:
        print(n // 2)
else:
    if n % 5 == 0:
        print(n // 5)
    elif n % 5 == 1 or n % 5 == 4:
        print(n // 5 + 2)
    elif n % 5 == 2:
        print(n // 5 + 1)
    else:
        print(n // 5 + 3)


# 진짜 그리드
cnt = 0

while n > 0:
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 2
        cnt += 1

if n < 0:
    print(-1)
else:
    print(cnt)
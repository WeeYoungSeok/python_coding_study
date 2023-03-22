# 팩토리얼 0의 개수
import math
n = int(input())

result = 0

fac_n = math.factorial(n)

while fac_n != 0:
    if fac_n % 10 == 0:
        result += 1
    else:
        break
    fac_n //= 10
print(result)
# 나누기

n = input()
f = int(input())

n = int(n[:-2] + "00")

while True:
    if n % f == 0:
        break
    n += 1

print(str(n)[-2:])
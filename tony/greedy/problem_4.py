# A -> B
a, b = map(int, input().split())

count = 0

while b > a:
    if b % 2 == 0:
        b //= 2
    else:
        if str(b)[-1] != "1":
            break
        b = int(str(b)[:-1])
    count += 1

if b != a:
    count = -2

print(count + 1)
# 숫자 새기
a = int(input())
b = int(input())
c = int(input())

l = list(map(int, str(a * b * c)))

for i in range(0, 10):
    print(l.count(i))
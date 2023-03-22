# 브루트포스 알고리즘
# 하나씩 순회하면서 찾아야한다.
n = int(input())
a = 666
cnt = 0
while n:
    if "666" in str(a):
        n -= 1
    a += 1

print(a-1)
n = int(input())

set_list = set()

for _ in range(n):
    x = input()
    set_list.add(x)

result = list(set_list)
result.sort()
result.sort(key=len)

for i in result:
    print(i)
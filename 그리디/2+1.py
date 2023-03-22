

n = int(input())

list = []

for i in range(n):
    x = int(input())
    list.append(x)
list.sort(reverse = True)

count = 0
new_list = []
result = 0
for i in list:
    new_list.append(i)
    count += 1
    if count > 2:
        new_list.sort()
        result += new_list[1] + new_list[2]
        new_list = []
        count = 0

for i in new_list:
    result += i

print(result)
import math

m = int(input())
n = int(input())

list = [False] * (n + 1)
bool = False
x = 0
for i in range(2, int(math.sqrt(n)) + 1):
    x += i
    while x < len(list):
        if x != i:
            list[x] = True
        x += i
    x = 0

new_list = []
for i in range(m, len(list)):
    if i == 0 or i == 1:
        continue
    if list[i] == False:
        new_list.append(i)
      
if len(new_list) == 0:
    print("-1")
else:
    print(sum(new_list))
    print(min(new_list))
           
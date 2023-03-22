import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

array = []
dict_n = {}
for _ in range(n):
    x = int(input())
    array.append(x)
    # if dict_n.get(x) == None:
    #     dict_n[x] = 1
    # else:
    #     dict_n[x] += 1
      
array.sort()
print(round(sum(array) / n))
print(array[int(len(array) / 2)])

dict_n = Counter(array).most_common()
if len(dict_n) > 1:
    if dict_n[0][1] == dict_n[1][1]:
        print(dict_n[1][0])
    else:
        print(dict_n[0][0])
else:
    print(dict_n[0][0])
# if len(dict_n) == 1:
#     print(array[0])
# else:
#     max_value = -1000000
#     dict_n = sorted(dict_n.items(), key=lambda x: x[1], reverse = True)
#     lst = []
#     for i in dict_n:
#         if i[1] >= max_value:
#             max_value = i[1]
#             lst.append(i[0])
#     lst.sort()
#     if len(lst) == 1:
#         print(lst[0])
#     else:
#         print(lst[1])
print(abs(min(array) - max(array)))


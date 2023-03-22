# import collections
import sys

# n = list(map(str, input()))
# n = [x.upper() for x in n]

# dict = collections.Counter(n)

# dict = sorted(dict.items() , reverse = True, key = lambda item : item[1])
# j = 0
# max = 0
# word = ""
# if len(dict) < 2:
#     print(dict[0][0])
# else:
#     if dict[0][1] == dict[1][1]:
#         print("?")
#     else:
#         print(dict[0][0])
# for i in dict.keys():
#     if j == 0:
#         max = dict.get(i)
#         word = i
#     if j == 1:
#         if max == dict.get(i):
#             print("?")
#             break
#         else:
#             print(word.upper())
#             break
#     j += 1

words = sys.stdin.readline().strip().upper()
set = list(set(words))

count_list = []
for i in set:
    count = words.count(i)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    max_index = count_list.index(max(count_list))
    print(set[max_index])
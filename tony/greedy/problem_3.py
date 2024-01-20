# 블로그2

from itertools import groupby

n = int(input())
words = list(input())

# 파이썬의 groupby 활용

# r_group_count = 0
# b_group_count = 0

# for letter, countLetter in groupby(words):
#     if letter == "R":
#         r_group_count += 1
#     else:
#         b_group_count += 1

# print(1 + min(r_group_count, b_group_count))

# 오리지널 코드
pre = ''
color_dict = {"R" : 0, "B" : 0}

for word in words:
    if pre != word:
        color_dict[word] += 1
    pre = word

print(1 + min(color_dict["R"], color_dict["B"]))

# 생태학
import sys

input = sys.stdin.readline

paper_dict = {}

while True:
    word = input().strip()
    if word == "":
        break
    if word not in paper_dict:
        paper_dict[word] = 1
    else:
        paper_dict[word] += 1

paper_dict = dict(sorted(paper_dict.items()))

sum_paper = sum(paper_dict.values())

for paper_name in paper_dict:
    print("%s %.4f" % (paper_name, paper_dict[paper_name] / sum_paper * 100))
import sys

input = sys.stdin.readline


# 반례
# [()][.   [(]. ([). ). ].
while True:
    x = input().rstrip()
    if x == ".":
        break
    array = []
    for i in x:
        if i == "(" or i == "[":
            array.append(i)
        elif i == ")":
            if len(array) == 0 or array[-1] != "(":
                print("no")
                break
            else:
                array.pop()
        elif i == "]":
            if len(array) == 0 or array[-1] != "[":
                print("no")
                break
            else:
                array.pop()
        if i == ".":
            if len(array) == 0:
                print("yes")
            else:
                print("no")
        
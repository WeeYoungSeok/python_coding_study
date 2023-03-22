import sys

input = sys.stdin.readline
stack = []

n = int(input())

for _ in range(n):
    x = input().strip()
    if "push" in x:
        stack.append(x.split()[1])
    elif x == "size":
        print(len(stack))
    elif x == "empty":
        if len(stack) != 0:
            print("0")
        else:
            print("1")
    elif x == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print("-1")
    elif x == "top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print("-1")
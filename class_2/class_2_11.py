import sys

input = sys.stdin.readline

n = int(input().strip())

for i in range(n):
    x = input().strip()
    array = []
    for j in x:
        if j == "(":
            array.append(j)
        else:
            if len(array) == 0:
                print("NO")
                break
            else:
                array.pop()
    else:
        if len(array) > 0:
            print("NO")
        else:
            print("YES")
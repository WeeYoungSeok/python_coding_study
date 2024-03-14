import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    t = input().strip()
    s = []
    for word in t:
        if word == "(":
            s.append(word)
        else:
            if len(s) != 0:
                if s[-1] != "(":
                    s.append(word)
                    break
                s.pop()
            else:
                s.append(word)
                break
    if len(s) == 0:
        print("YES")
    else:
        print("NO")
                    

        
            


    
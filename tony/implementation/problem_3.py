# 단어 뒤집기2
import sys
input = sys.stdin.readline

s = list(input().strip())
i = 0

while i < len(s):
    if s[i] == "<":
        while s[i] != ">":
            i += 1
        i += 1
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        temp = s[start:i]
        temp.reverse()
        s[start:i] = temp
    else:
        i += 1
        

print("".join(s))



# 원래 내 풀이

import sys

input = sys.stdin.readline

s = input().strip()

st = []
bool = False

result = ""

for word in s:
    if word == "<":
        while len(st) > 0:
            result += st.pop()
        bool = True
        result += word
    else:
        if bool == True:
            result += word
            if word == ">":
                bool = False
        else:
            if word == " ":
                if len(st) > 0:
                    while len(st) > 0:
                        result += st.pop()
                result += word
            else:
                st.append(word)

while len(st) > 0:
    result += st.pop()

print(result)



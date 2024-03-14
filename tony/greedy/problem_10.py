# 내 풀이
import sys

input = sys.stdin.readline

words = input().strip()

temp = ""
result = ""

for word in words:
    if word == ".":
        if temp != "":
            if temp.count("X") % 2 != 0:
                break
            else:
                if temp.count("X") == 4:
                    result += "AAAA"
                else:
                    result += "BB"
                temp = ""
        result += "."
    else:
        temp += word
        if temp.count("X") == 4:
            result += "AAAA"
            temp = ""

if temp.count("X") % 2 != 0:
    result = -1
else:
    if temp.count("X") == 2:
        result += "BB"

print(result)


# 다른 사람 풀이
board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB") 

if 'X' in board:
    print(-1)
else:
    print(board)

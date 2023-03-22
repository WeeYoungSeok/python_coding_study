# 체스판

white_black = [0, 1, 0, 1, 0, 1, 0 ,1]

answer = 0

for i in range(8):
    chess = input()
    for j in range(8):
        if i % 2 == 0:
            if white_black[j] == 0 and chess[j] == "F":
                answer += 1
        else:
            if white_black[7 - j] == 0 and chess[j] == "F":
                answer += 1

print(answer)
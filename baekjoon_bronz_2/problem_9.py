# 농구 경기
n = int(input())

players = []
answer = ""
for _ in range(n):
    players.append(input()[0])

for i in range(97, 123):
    if players.count(chr(i)) >= 5:
        answer += chr(i)

if answer == "":
    print("PREDAJA")
else:
    print(answer)
# 백준 풍선 터뜨리기

n = int(input())
balloons = list(map(int, input().split()))
booms = [False] * n
booms[0] = True

result = [1]

boom = 0

while True:
    move = balloons[boom]
    while move != 0:
        if move > 0:
            temp_boom = boom + 1
            if temp_boom == n:
                temp_boom = 0
            boom = temp_boom
            if booms[temp_boom] == False:
                move -= 1
        if move < 0:
            temp_boom = boom - 1
            if temp_boom == -1:
                temp_boom = n - 1
            boom = temp_boom
            if booms[temp_boom] == False:
                move += 1

    booms[boom] = True
    result.append(boom + 1)
    if booms.count(True) == n:
        break

print(" ".join(map(str, result)))
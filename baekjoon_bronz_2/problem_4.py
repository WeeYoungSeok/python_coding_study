# 펫
i = 1

while True:
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break
    die_flag = False
    while True:
        x, y = input().split()
        if x == "#" and y == "0":
            break
        else:
            if x == "E":
                w -= int(y)
            else:
                w += int(y)
        if w <= 0:
            die_flag = True
    if bool == True:
        break
    if die_flag == True:
        print(i, "RIP")
    elif w > o * 0.5 and w < o * 2:
        print(i, ":-)")
    else:
        print(i, ":-(")
    i += 1
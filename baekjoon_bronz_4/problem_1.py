# 모음의 개수
mo = ["a", "e", "i", "o", "u"]

while True:
    word = input() 
    if word == "#":
        break
    count = 0
    for m in mo:
        upper_m = m.upper()
        count += word.count(m)
        count += word.count(upper_m)
    print(count)
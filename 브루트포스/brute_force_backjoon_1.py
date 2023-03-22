# 마인크래프트
n, m, b = map(int, input().split())

time = int(1e9)
result = 0

earth = []

for _ in range(n):
    earth.append(list(map(int, input().split())))

for i in range(257):
    use_block = 0
    inven_block = 0
    for j in range(n):
        for k in range(m):
            if earth[j][k] < i:
                use_block += (i - earth[j][k])
            else:
                inven_block += (earth[j][k] - i)
    # 사용된 블록이 인벤에 있는 블록보다 크다면 만들 수 없음
    if use_block > b + inven_block:
       continue
    # 시간
    count = (inven_block * 2) + use_block
    # 시간이 같을 때 높이가 높은 순으로 나와야하므로 =을 붙여주어야한다.
    if count <= time:
        time = count
        result = i
print(time, result)
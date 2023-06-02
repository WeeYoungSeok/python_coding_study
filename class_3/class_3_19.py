# Z

N, r, c = map(int, input().split())

result = 0

while N != 0:

    N -= 1

    v = 2 ** N

    # 1사분면
    if r < v and c < v:
          result += v * v * 0
    # 2사분면
    elif r < v and c >= v:
          result += v * v * 1
          c -= v
    # 3사분면
    elif r >= v and c < v:
          result += v * v * 2
          r -= v
    # 4사분면
    else:
        result += v * v * 3
        r -= v
        c -= v

print(result)
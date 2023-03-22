n = int(input())

if n < 9:
    print(0)
else:
    answer = 0
    cnt = 1
    for _ in range(9, n + 1, 3):
        answer += cnt
        cnt += 1
    print(answer)
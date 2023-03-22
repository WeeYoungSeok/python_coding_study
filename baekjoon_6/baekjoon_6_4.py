n = int(input())

for i in range(n):
    count, word = map(str, input().split())
    result = ""
    for j in word:
        for k in range(int(count)):
            result += j
    print(result)    
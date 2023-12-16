n = int(input())

t = list(map(int, input().split()))

t.sort()

result = []

if len(t) % 2 != 0:
    result.append(t.pop(-1))

for i in range(len(t) // 2):
    # result.append(t[i] + t[len(t) -1 -i])
    result.append(t[i] + t[-i -1])

print(max(result))
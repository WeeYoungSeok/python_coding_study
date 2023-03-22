import sys
n = int(sys.stdin.readline())

array = []
for i in range(n):
    rop = int(sys.stdin.readline())
    array.append(rop)

array.sort(reverse = True)

answer = []

for i in range(n):
    answer.append(array[i] * (i + 1))

print(max(answer))
  
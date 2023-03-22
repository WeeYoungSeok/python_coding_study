x = int(input())

array = []
for i in range(x):
    one, two = map(int, input().split())
    array.append(one + two)

for i in array:
    print(i, end = "\n")
array = [[0 for col in range(19)] for row in range(19)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    array[x - 1][y - 1] = 1

for i in array:
    for j in i:
        print(j, end = " ")
    print()
               
x = int(input())
y = input()

for i in range(len(y) -1, -1, -1):
    print(x * int(y[i]))

print(x * int(y))
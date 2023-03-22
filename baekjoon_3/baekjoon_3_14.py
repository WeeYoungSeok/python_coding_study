x = input()

if len(x) == 1:
    x = "0" + x
  
result = 0
oldX = x

while True:
    plus = str(int(x[0]) + int(x[1]))
    if len(plus) == 1:
        x = x[1] + plus
    else:
        x = x[1] + plus[1]
    result += 1
    if x == oldX:
        break

print(result)
    
n = int(input())
oldN = n
i = 1

while n > i:
    n -= i
    i += 1

if i % 2 == 0:
    x, y = 1, i
else:
    x, y = i, 1
  
count = oldN - ((i * (i -1)) // 2) - 1

for a in range(count):
    if i % 2 == 0:
        x += 1
        y -= 1
    else:
        x -= 1
        y += 1
print(str(x) + "/" + str(y))
    
    
  
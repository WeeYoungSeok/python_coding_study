n = int(input())

if n % 2 == 0:
    if n < 0:
        print("A")
    else:
        print("C")
else:
    if n < 0:
        print("B")
    else:
        print("D")
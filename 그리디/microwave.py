n = int(input())

array = [300, 60, 10]

if n % array[2] != 0:
    print("-1")
else:
    for i in range(len(array)):
        if n // array[i] > 0:
            print(n // array[i], end = " ")
            n %= array[i]
        else:
            print("0", end = " ")
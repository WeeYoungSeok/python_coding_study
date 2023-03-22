result = 0

max = 0
maxIndex = 0

while result < 9:
    result += 1
    number = int(input())
    if number > max:
        max = number
        maxIndex = result

print("{}\n{}".format(max, maxIndex))
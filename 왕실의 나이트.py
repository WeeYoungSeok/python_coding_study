# 왕실의 나이트

col_y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

n = input()

x = int(n[1]) - 1
y = int(col_y.index(n[0]))

result = 0

for i in range(8):
    if i == 0:
        nx = x - 2
        ny = y + 1
    elif i == 1:
        nx = x - 2
        ny = y - 1
    elif i == 2:
        nx = x + 2
        ny = y + 1
    elif i == 3:
        nx = x + 2
        ny = y - 1
    elif i == 4:
        nx = x + 1
        ny = y - 2
    elif i == 5:
        nx = x - 1
        ny = y - 2
    elif i == 6:
        nx = x + 1
        ny = y + 2
    else:
        nx = x - 1
        ny = y + 2
    if nx >= 0 and ny >= 0 and nx <= 7 and ny <= 7:
        result += 1

print(result)


# 나동빈님 코드

input_data = input()

row = int(input_data[1]) - 1
col = int(ord(input_data[0])) - int(ord('a'))

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row >= 0 and next_col >= 0 and next_row <= 7 and next_col <= 7:
        result += 1
print(result)
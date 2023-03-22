# 색종이 자르기
n = int(input())

square = []
blue = 0
white = 0

for _ in range(n):
    square.append(list(map(int, input().split())))
  
def square_check(x, y, n):
    global blue
    global white

    # 처음 색 
    check_value = square[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if square[i][j] != check_value:
                square_check(x, y, n // 2)
                square_check(x, y + n // 2, n // 2)
                square_check(x + n // 2, y, n // 2)
                square_check(x + n // 2, y + n // 2, n // 2)
                return

    if check_value == 1:
        blue += 1
    else:
        white += 1
    

square_check(0, 0, n)
print(white)
print(blue)
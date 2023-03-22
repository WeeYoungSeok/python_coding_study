# 직사각형 넓이 구하기
# 가장 큰 x좌표 - 가장 작은 x좌표 = 가로 길이
# 가장 작은 y좌표 - 가장 작은 y좌표 = 세로 길이
def solution(dots):
    width = max(dots, key=lambda x : x[0])[0] - min(dots,  key=lambda x : x[0])[0]
    height = max(dots, key=lambda x : x[1])[1] - min(dots,  key=lambda x : x[1])[1]
    return width * height
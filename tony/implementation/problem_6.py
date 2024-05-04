# 백준 오목
# 내 풀이
baduk = []
bool = False
len_count = 1
width_count = 1
dia_count = 1
dia_count1 = 1

for _ in range(19):
    baduk.append(list(map(int, input().split())))


def len_baduk_right(num, i, j):
    global len_count
    right_x = i + 1
    if right_x > 18:
        return
    else:
        if baduk[right_x][j] == num:
            len_count += 1
            len_baduk_right(num, right_x, j)
        else:
            return


def len_baduk_left(num, i, j):
    global len_count
    left_x = i - 1
    if left_x < 0:
        return
    else:
        if baduk[left_x][j] == num:
            len_count += 1
            len_baduk_left(num, left_x, j)
        else:
            return


def width_baduk_right(num, i, j):
    global width_count
    right_y = j + 1
    if right_y > 18:
        return
    else:
        if baduk[i][right_y] == num:
            width_count += 1
            width_baduk_right(num, i, right_y)
        else:
            return


def width_baduk_left(num, i, j):
    global width_count
    left_y = j - 1

    if left_y < 0:
        return
    else:
        if baduk[i][left_y] == num:
            width_count += 1
            width_baduk_left(num, i, left_y)
        else:
            return


def diagonal_baduk_right(num, i, j):
    global dia_count
    right_x = i + 1
    right_y = j + 1

    if right_x > 18 or right_y > 18:
        return
    else:
        if baduk[right_x][right_y] == num:
            dia_count += 1
            diagonal_baduk_right(num, right_x, right_y)
        else:
            return


def diagonal_baduk_left(num, i, j):
    global dia_count
    right_x = i - 1
    right_y = j - 1

    if right_x < 0 or right_y < 0:
        return
    else:
        if baduk[right_x][right_y] == num:
            dia_count += 1
            diagonal_baduk_left(num, right_x, right_y)
        else:
            return


def diagonal_baduk_right1(num, i, j):
    global dia_count1
    right_x = i + 1
    right_y = j - 1

    if right_x > 18 or right_y < 0:
        return
    else:
        if baduk[right_x][right_y] == num:
            dia_count1 += 1
            diagonal_baduk_right1(num, right_x, right_y)
        else:
            return


def diagonal_baduk_left1(num, i, j):
    global dia_count1
    right_x = i - 1
    right_y = j + 1

    if right_x < 0 or right_y > 18:
        return
    else:
        if baduk[right_x][right_y] == num:
            dia_count1 += 1
            diagonal_baduk_left1(num, right_x, right_y)
        else:
            return


# def diagonal_baduk(num, i, j, count):
#     # 대각 검사 (오른쪽 아래로 검사)
#     if i + 1 <= 3 and j + 1 <= 3:
#         if baduk[i + 1][j + 1] == num:
#             count += 1
#             return diagonal_baduk(num, i + 1, j + 1, count)
#     return count

for i in range(len(baduk)):
    for j in range(len(baduk[i])):
        if baduk[i][j] != 0:
            len_baduk_right(baduk[i][j], i, j)
            len_baduk_left(baduk[i][j], i, j)
            width_baduk_right(baduk[i][j], i, j)
            width_baduk_left(baduk[i][j], i, j)
            diagonal_baduk_right(baduk[i][j], i, j)
            diagonal_baduk_left(baduk[i][j], i, j)
            diagonal_baduk_right1(baduk[i][j], i, j)
            diagonal_baduk_left1(baduk[i][j], i, j)
            if width_count == 5 or len_count == 5 or dia_count == 5:
                print(baduk[i][j])
                print(i + 1, j + 1)
                bool = True
                break
            elif dia_count1 == 5:
                print(baduk[i][j])
                print(i + 5, j - 3)
                bool = True
                break
            width_count = 1
            len_count = 1
            dia_count = 1
            dia_count1 = 1
    if bool:
        break

if not bool:
    print(0)

# bfs 제대로 이용
import sys

input = sys.stdin.readline

baduk = []

for _ in range(19):
    baduk.append(list(map(int, input().split())))

# 가로, 세로, 오른쪽 아래 대각, 왼쪽 위로 대각
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(len(baduk)):
    for y in range(len(baduk[x])):
        if baduk[x][y] != 0:
            for i in range(4):
                count = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < len(baduk) and 0 <= ny < len(
                        baduk[x]) and baduk[nx][ny] == baduk[x][y]:
                    count += 1

                    if count == 5:
                        # 첫 바둑돌 이전에 같은 바둑돌이 있다면
                        if 0 <= x - dx[i] < len(
                                baduk) and 0 <= y - dy[i] < len(
                                    baduk[x]) and baduk[x - dx[i]][
                                        y - dy[i]] == baduk[x][y]:
                            break
                        # 마지막 바둑돌 다음에 같은 바둑돌이 있다면
                        if 0 <= nx + dx[i] < len(
                                baduk) and 0 <= ny + dy[i] < len(
                                    baduk[x]) and baduk[nx + dx[i]][
                                        ny + dy[i]] == baduk[x][y]:
                            break
                        print(baduk[x][y])
                        print(x + 1, y + 1)
                        sys.exit(0)
                    nx += dx[i]
                    ny += dy[i]

print(0)

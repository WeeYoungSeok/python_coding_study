# 캐릭터의 좌표
def solution(keyinput, board):
    answer = []
    # 동 북 서 남
    move_types = ["right", "up", "left", "down"]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x, y = 0, 0
    for key in keyinput:
        for i in range(len(move_types)):
            if key == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= -(board[0] // 2) and nx <= board[0] // 2 and ny >= -(board[1] // 2) and ny <= board[1] // 2:
                    x, y = nx, ny
    answer.append(x)
    answer.append(y)
    return answer
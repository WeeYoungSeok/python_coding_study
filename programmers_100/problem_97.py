# 안전지대
def solution(board):
    # 최대 안전지대
    answer = len(board) * len(board[0])
    # 동 북 서 남 오위대 오아래대 왼위대 왼아래대
    dx = [0, 1, 0, -1, 1, -1, 1, -1]
    dy = [1, 0, -1, 0, 1, 1, -1, -1]
    for i in range(len(board)):
        for j in range(len(board[i])):
            # 주위가 0일때만 -1로 만들면서 안전지대 갯수 줄이기
            if board[i][j] == 1:
                answer -= 1
                for k in range(len(dx)):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    # 범위 검사 및 0검사
                    if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]) and board[nx][ny] == 0:
                        board[nx][ny] = -1
                        answer -= 1
    return answer
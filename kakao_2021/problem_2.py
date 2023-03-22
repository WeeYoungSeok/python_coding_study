# 거리두기 확인하기
def solution(places):
    answer = []
    # 동 북 서 남 
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for place in places:
        bool = True
        for i in range(len(place)):
            for j in range(len(place[i])):
                # 사람이라면 검사
                if place[i][j] == "P":
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        # 범위 밖으로 안나갔다면 추가 검사
                        if nx >= 0 and nx <= 4 and ny >= 0 and ny <= 4:
                            # 만약 사람이라면 거리두기 실패
                            if place[nx][ny] == "P":
                                answer.append(0)
                                bool = False
                            # 빈테이블이라면 추가 검사
                            elif place[nx][ny] == "O":
                                for h in range(4):
                                    new_x = nx + dx[h]
                                    new_y = ny + dy[h]
                                    # 기존에 검사했던 곳이 아니면서 범위 안이라면
                                    if new_x != i and new_y != j and new_x >= 0 and new_x <= 4 and new_y >= 0 and new_y <= 4:
                                        # 빈테이블 주위에 사람이 있다면 실패
                                        if place[new_x][new_y] == "P":
                                            answer.append(0)
                                            bool = False
                        if bool == False:
                            break
                if bool == False:
                    break
            if bool == False:
                break
        answer.append(1)        
    return answer
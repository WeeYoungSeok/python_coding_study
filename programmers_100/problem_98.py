# 겹치는 선분의 길이
def solution(lines):
    answer = 0
    duple_lines = []
    # 겹치는 곳을 찾는다.
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            # 겹치는 조건
            if lines[i][0] < lines[j][1] and lines[i][1] > lines[j][0]:
                duple_lines.append([max(lines[i][0], lines[j][0]), min(lines[i][1], lines[j][1])])
    if len(duple_lines) == 0:
        return 0
    triple_lines = []
    for i in range(len(duple_lines) - 1):
        for j in range(i + 1, len(duple_lines)):
            # 겹치는 조건
            if duple_lines[i][0] < duple_lines[j][1] and duple_lines[i][1] > duple_lines[j][0]:
                triple_lines.append([max(duple_lines[i][0], duple_lines[j][0]), min(duple_lines[i][1], duple_lines[j][1])])
    # 겹치는 것만 더하기
    for duple in duple_lines:
        answer += (duple[1] - duple[0])
    # 세 곳이 겹치는 라인은 빼주기
    if len(triple_lines) > 0:
        for _ in range(2):
            answer -= (triple_lines[0][1] - triple_lines[0][0])
    return answer
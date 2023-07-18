# 최소직사각형
def solution(sizes):
    for i in range(0, len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    max_width = 0
    max_hight = 0

    for i in range(0, len(sizes)):
        max_width = max(max_width, sizes[i][0])

    for i in range(0, len(sizes)):
        max_hight = max(max_hight, sizes[i][1])
            
    return max_width * max_hight

# 더 간단한 풀이
def solution(sizes):
    max_width = 0
    max_hight = 0
    
    for i in range(0, len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        max_width = max(max_width, sizes[i][0])
        max_hight = max(max_hight, sizes[i][1])
            
    return max_width * max_hight
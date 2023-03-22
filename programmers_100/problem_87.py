# 삼각형의 완성 조건(2)
def solution(sides):
    answer = 0
    max_sides = max(sides)
    idx = sides[0] if sides.index(max_sides) > 0 else sides[1]
    # 가장 긴 변이 배열에 있는 경우
    for i in range(1, max_sides + 1):
        if i + idx > max_sides:
            answer += 1
    # 가장 긴 변이 배열에 없는 경우
    answer += ((max_sides + idx) - (max_sides + 1))
    return answer

# 수학적 풀이
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1
# 달력
# 내 풀이
import sys

input = sys.stdin.readline

n = int(input())
plans = []

for _ in range(n):
    plans.append(list(map(int, input().split())))

plans.sort(key=lambda x: (x[0], -x[1]))

cals = [[0 for _ in range(max(map(max, plans)) + 1)]]

for plan in plans:
    bool = False
    # 시작일부터 끝날까지 모든 달력을 돌면서 만약 하나라도 채워져있다면 다음줄로 가야됨
    for i in range(len(cals)):
        already_bool = False
        for day in range(plan[0], plan[1] + 1):
            # 일정 기간중에 이미 채워져 있다면
            # 해당 줄은 쓰지 못함
            if cals[i][day] != 0:
                already_bool = not already_bool
                break
        # 만약 해당 줄에 스케줄이 채워져 있지 않다면 채우기
        if not already_bool:
            for day in range(plan[0], plan[1] + 1):
                cals[i][day] = 1
            bool = True
            break
    if not bool:
        # 만약 스케줄을 채우지 못했다면 줄 추가 후 스케줄 채우기
        cals.append([0 for _ in range(max(map(max, plans)) + 1)])
        for day in range(plan[0], plan[1] + 1):
            cals[-1][day] = 1

# 코팅지
result = 0
day = 1
start = 0
hei = 0

while day < len(cals[0]):
    bool = False
    for i in range(len(cals)):
        if cals[i][day] == 1:
            bool = True
            if start == 0:
                start = day
            if hei < i:
                hei = i
    # 연속되지 않았다면 코팅지 오려야됨
    if not bool and start > 0:
        result += ((day - start) * (hei + 1))
        start = 0
        hei = 0
    day += 1

if start > 0:
    result += ((day - start) * (hei + 1))
print(result)





# 다른 풀이 (시간 단축 + 코드 깔끔)
import sys
input = sys.stdin.readline

n = int(input())
plans = [list(map(int, input().split())) for _ in range(n)]
plans.sort()
calendar = [0] * 366

for start, end in plans:
    for day in range(start, end + 1):
        calendar[day] += 1

max_height = 0
total_area = 0
current_width = 0

# 각 날짜별로 달력을 검사하면서 연속된 스케줄이 있는 영역을 찾고 해당 영역의 높이와 너비를 계산하여 총 면적을 구합니다.
for day in range(1, 366):
    # 현재 날짜에 스케줄이 없는 경우를 확인합니다. (calendar 리스트에서 해당 날짜의 값이 0인 경우)
    if calendar[day] == 0:
        # 현재까지의 연속된 스케줄 영역의 면적을 총 면적에 추가합니다.
        # 여기서 max_height는 현재까지의 최대 높이이고, current_width는 현재까지의 연속된 스케줄의 너비입니다.
        total_area += max_height * current_width

        # 연속된 스케줄 영역의 높이와 너비를 초기화합니다.
        # 현재까지의 스케줄 영역이 끝났기 때문에 이 값들을 초기화해야 합니다.
        max_height = 0
        current_width = 0
    else:
        # 현재 날짜에 스케줄이 있는 경우를 처리합니다.

        # 현재까지의 최대 높이와 현재 날짜의 스케줄 높이 중 더 큰 값을 선택하여 최대 높이를 업데이트합니다.
        max_height = max(max_height, calendar[day])

        # 현재까지의 연속된 스케줄의 너비를 1 증가시킵니다.
        current_width += 1

# 마지막으로, 마지막 스케줄 영역의 면적을 총 면적에 추가합니다.
total_area += max_height * current_width
print(total_area)

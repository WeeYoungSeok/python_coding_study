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
        





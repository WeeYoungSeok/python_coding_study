n = int(input())
x = list(map(int, input().split()))

x.sort()

count = 0

while(True):
    target = x[0]
    if target == 0:
        x = x[1 : len(x)]
        count += 1
    else:
        if target <= len(x):
            if max(x[0 : target]) <= target:
                x = x[target : len(x)]
                count += 1
            else:
                break
        else:
            break 
    if len(x) == 0:
      break

print(count)

n = int(input())
x = list(map(int, input().split()))

x.sort()

# 결과 값
result = 0
# 현재 그룹에 포함된 모험가 수
count = 0

for i in x:
  # 한번 돌때 모험가를 한명 집어 넣음
  count += 1
  if count >= i: # 현재 그룹에 포함되어있는 모험가의 수가 현재 확인하고있는 공포도보다 크거나 그룹 결성
      result += 1
      count = 0

print(result)
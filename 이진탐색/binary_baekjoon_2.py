# 랜선 자르기
# 랜선 자르기 같은 경우에는 나누기가 들어가므로
# 나무 자르기나 떡 자르기처럼 마이너스가 아니다
# 고로 ZeroDivisionError를 생각해야 한다.
n, m = map(int, input().split())

lans = []
for _ in range(n):
    lans.append(int(input()))

# ZeroDivisionError를 방지하기 위해 start를 0이 아닌 1로 시작
start = 1
end = max(lans)
result = 0

while start <= end:
    mid = (start + end) // 2
    # 1, 1, 1일 경우 0으로 나눠지므로 ZeroDivisionError발생
    # 여기서 이렇게 처리해줘도 되지만 항상 if문을 검사해 효율이 안좋다
    # if mid == 0:
    #     result = 1
    #     break
    count = 0
    for lan in lans:
        if lan >= mid:
            count += (lan // mid)
    if count < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)
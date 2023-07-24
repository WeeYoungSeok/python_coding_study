# 시작점과 끝점 2개의 점으로 접근할 데이터의 범위 표현
# 2, 3, 4, 5, 6, 7 이라고 할떄 2부터 7까지라고 표현

data = [1, 2, 3, 2, 5]

# 합이 m인 부분 연속 수열의 개수

# m = 5라면 1 + 2 + 3 이런식으로 연속된 수를 찾아서
# 그 값이 넘거나 뭐 연속되지 않으면
# 다시 2부터 찾고 이러면 O(N^2)이 걸리게 된다

# 이럴떄 O(N)으로 시간 복잡도를 줄이고 싶을 때
# 투 포인터 알고리즘을 사용한다.

# 1. 시작점과 끝점이 첫 번째 원소의 인덱스(0)을 가리키도록 한다.
# 2. 현재 부분 합이 M과 같다면, 카운트
# 3. 현재 부분 합이 M보다 작다면, end를 1증가 시킨다.
# 4. 현재 부분 합이 M보다 크거나 같다면, start를 1증가
# 5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정 반복

# 내 코드
m = 5

start, end = 0, 0

count = 0
while start < len(data) and end < len(data):
    if sum(data[start:end + 1]) == m:
        count += 1
        start += 1
    elif sum(data[start:end + 1]) < m:
        end += 1
    else:
        start += 1

print(count)


# 이코테 코드

n = 5
m = 5

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
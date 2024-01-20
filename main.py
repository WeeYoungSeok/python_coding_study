# 행복 유치원

# 이해하기 상당히 빡세고
# 방법을 찾은 사람들이 대단할뿐이다..

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
st = list(map(int, input().split()))
diff = []

for i in range(n - 1):
    diff.append(st[i + 1] - st[i])

# 내림차순 정렬시
diff.sort(reverse=True)

print(sum(diff[k - 1:n - 1]))

# 오름차순 정렬시
diff.sort()

print(sum(diff[0:n - k]))
# 나무 자르기
n, m = map(int, input().split())
trees = list(map(int, input().split()))

result = 0
start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for tree in trees:
        if tree > mid:
            count += (tree - mid)
    if count < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
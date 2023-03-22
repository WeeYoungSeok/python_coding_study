# n = int(input())

# list = list(map(int, input().split()))

# list.sort(reverse = True)

# count = 1
# result = 0

# for i in list:
#     count += 1
#     if result > 0:
#         result -= 1
#     if result < i:
#         result = i
# print(count + result)

namu = input()
tree = list(sorted(map(int,input().split(" ")), reverse=True))
for j in range(len(tree)):
    tree[j] += j+1
print(max(tree)+1)
    
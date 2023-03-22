n, m = map(int, input().split())

array = set()

for _ in range(n):
    array.add(input())

array2 = set()
for _ in range(m):
    array2.add(input())

dule_array = array & array2

print(len(array & array2))

for word in sorted(dule_array):
    print(word)
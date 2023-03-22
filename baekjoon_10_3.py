n = int(input())
people = []
for _ in range(n):
    x = list(map(int, input().split()))
    people.append(x)

for i in range(len(people)):
    count = 0
    for j in range(len(people)):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    print(count + 1, end = " ")
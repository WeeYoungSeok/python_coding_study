# 읽어버린 괄호
s = input()

s_array = s.split("-")

answer = 0

for num in s_array[0].split("+"):
    answer += int(num)

for i in range(1, len(s_array)):
    for num in s_array[i].split("+"):
        answer -= int(num)

print(answer)

# 다른 풀이
s = input()

s_array = s.split("-")
answer = 0
i = 0

while i < len(s_array):
    if "+" in s_array[i]:
        list = s_array[i].split("+")
        if i == 0:
            answer += sum(map(int, list))
        else:
            answer += -sum(map(int, list))
    else:
        if i == 0:
            answer += int(s_array[i])
        else:
            answer += -int(s_array[i])
    i += 1

print(answer)
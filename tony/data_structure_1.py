# 탑
import sys

input = sys.stdin.readline

n = int(input().strip("\n"))
    
answer = [0 for _ in range(0, n)]

razers = list(map(int, input().strip("\n").split()))
s = []

for i in range(0, len(razers)):
    if len(s) == 0:
        s.append([razers[i], i + 1])
        continue
    while len(s) > 0:
        pop_data = s.pop()
        if pop_data[0] > razers[i]:
            answer[i] = pop_data[1]
            s.append(pop_data)
            s.append([razers[i], i + 1])
            break
        else:
            if len(s) == 0:
                s.append([razers[i], i + 1])
                break
                
print(" ".join(map(str, answer)))
# 이거때매 통과 안됐었음 배열 그대로 출력 아님
# 문제 똑바로 읽자..
# print(answer)
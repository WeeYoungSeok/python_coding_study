# 시간
import time

n = int(input())

result = 0
minute = 0
j = 0

start = time.time()
for i in range(n + 1):
    if str(3) in str(i):
        result += 3600
    else:
        while(True):
            if j == 60:
                minute = minute + 1         
                j = 0
            else:
                if str(3)in str(minute):
                    result += 60
                    minute = minute + 1  
                    j = 0
                else:
                    if str(3) in str(j):
                        result += 1
            if minute >= 60:
                minute = 0
                break
            j += 1

end = time.time()
print(end - start)
print(result)

# 나동빈님 코드
result = 0
start = time.time()

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                result += 1
end = time.time()
print(end - start)
print(result)
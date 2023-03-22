x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1: #1은 소수가 아뉘지!
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)

# else문은 for - else다
# for - else는 for문을 다돌면 else부분이 실행되고
# break를 만나면 for - else의 else가 실행이 되지 않는다.
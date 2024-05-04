# 백준 오리
sound = list(input())
ans = 0
quack = "quack"
j = 0

if sound[0] != "q"  or  sound[-1] != "k" or len(sound) % 5 :
    print(-1)
    exit()

for i in range(len(sound)):     
    if sound[i] == "q":
        new_ori = True
        for i in range(i, len(sound)):
            if sound[i] == quack[j]:
                if sound[i] == "k":
                    if new_ori:  
                        ans += 1
                        new_ori = False           
                    j = 0         
                    sound[i] = 0           
                    continue        
                j += 1
                sound[i] = 0


if any(sound) or ans == 0 :
    print(-1)
else:
    print(ans)
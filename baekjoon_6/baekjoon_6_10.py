n = int(input())

count = 0
bool = True
for i in range(n):
    word = input()
    if len(word) <= 2:
        count += 1
        continue
    else:
        for x in word:
            index = word.find(x)
            lastIndex = len(word) - 1 -"".join(reversed(word)).find(x)
            list = word[index:lastIndex + 1]
            if list.count(x) != len(list):
                bool = False
                break
    if bool == True:
        count += 1
    bool = True 
print(count)
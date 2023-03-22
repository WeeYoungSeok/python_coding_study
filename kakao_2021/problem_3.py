def solution(n, k, cmd):
    answer = ''
    origin_array = []
    new_array = []
    recent_del = []
    for i in range(n):
        origin_array.append(i)
        new_array.append(i)
    for word in cmd:
        if word[0] == "D":
            k += int(word[2])
            if k >= n:
                k = n - 1
        elif word[0] == "U":
            k -= int(word[2])
            if k < 0:
                k = 0
        elif word[0] == "C":
            del new_array[k]
            recent_del.append(k)
        else:
            if len(recent_del) > 0:
              new_array.insert(recent_del[0], (recent_del[0])
    print(new_array)
    return answer
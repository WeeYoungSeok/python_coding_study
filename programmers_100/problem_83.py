# 컨트롤 제트
def solution(s):
    s = s.split()
    while "Z" in s:
        z_value = s.index("Z")
        del s[z_value]
        if z_value > 0:
            if not s[z_value - 1].isalpha():
                del s[z_value - 1]
    return sum(s)

# stack으로 풀기
def solution(s):
    arr = s.split(' ')
    result =[]
    for i in arr :
        # Z로 시작하는 경우에는 에러가 난다.
        if i=='Z':
            # 따라서 예외를 잡아준다.
            try:
                result.pop()
            except:
                continue
        else:
            result.append(int(i))
    return sum(result)
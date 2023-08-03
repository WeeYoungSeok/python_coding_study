# 올바른 괄호
def solution(s):
    answer = True
    st = []

    for word in s:
        if word == ")":
            if len(st) == 0:
                answer = False
                break
            else:
                if st.pop() != "(":
                    answer = False
                    break
        else:
            st.append(word)

    if len(st) > 0:
        answer = False
        
    return answer
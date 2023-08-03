# 괄호 회전하기
def solution(s):
    answer = 0
    for _ in range(len(s)):
        # 올바른 괄호 검사
        st = []
        bool = True
        for word in s:
            if word == ")" or word == "]" or word == "}":
                if len(st) == 0:
                    bool = False
                    break
                else:
                    if word == ")":
                        if st.pop() != "(":
                            bool = False
                            break
                    elif word == "]":
                        if st.pop() != "[":
                            bool = False
                            break
                    elif word == "}":
                        if st.pop() != "{":
                            bool = False
                            break
            else:
                st.append(word)
        if len(st) == 0 and bool == True:
            answer += 1
        s += s[0]
        s = s[1:len(s)]
        bool = True
                
    return answer
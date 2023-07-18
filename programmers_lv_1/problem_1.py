# 신규 아이디

# 원래 풀이
def solution(new_id):
    answer = ''
    # ., -, _ 포함 여부 배열
    special = [".", "-", "_"]
    # step 1 : 소문자로 변경
    new_id = new_id.lower()
    # step 2 ~ 4
    for char in new_id:
        if len(answer) == 0:
            if char != "." and (char == "_" or char == "-" or char.isdigit()
                                or char.isalpha()):
                answer += char
        else:
            if char in special or char.isdigit() or char.isalpha():
                if char == "." and answer[len(answer) - 1] == ".":
                    continue
                else:
                    answer += char

    answer = answer.strip(".")

    # step 5 ~ 7
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[len(answer) - 1] == ".":
            answer = answer[:-1]
    else:
        if len(answer) == 0:
            answer = "a"
        if len(answer) <= 2:
            while len(answer) < 3:
                answer += answer[-1]
    return answer

# 고친 풀이
def solution(new_id):
    answer = ''
    # ., -, _ 포함 여부 배열
    special = [".", "-", "_"]
    
    # step 1 : 소문자로 변경
    new_id = new_id.lower()
    
    # step 2
    for char in new_id:
        if char in special or char.isdigit() or char.isalpha():
            answer += char

    # step 3
    while ".." in answer:
        answer = answer.replace("..", ".")
    
    # step 4
    answer = answer.strip(".")

    # step 5
    if len(answer) == 0:
            answer = "a"
    
    # step 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[len(answer) - 1] == ".":
            answer = answer[:-1]
    # step 7
    else:
        while len(answer) < 3:
            answer += answer[-1]
    return answer
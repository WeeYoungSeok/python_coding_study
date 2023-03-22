# A로 B 만들기
def solution(before, after):
    for word in before:
        if word in after:
            after = after.replace(word, "", 1)
    if len(after) == 0:
        return 1
    return 0

# 파이썬은 리스트의 요소와 순서가 같은 리스트끼리 == 연산자로 True가 리턴된다.
# sorted로 풀기
def solution1(before, after):
    return 1 if sorted(before) == sorted(after) else 0
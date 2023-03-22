# OX 퀴즈
def solution(quiz):
    answer = []
    for word in quiz:
        quiz_list = word.split(" = ")
        if eval(quiz_list[0]) == int(quiz_list[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer

# valid로 풀기..
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]   
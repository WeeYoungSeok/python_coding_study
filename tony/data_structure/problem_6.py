# 후위 표기법 2
import sys

input = sys.stdin.readline

oper = ["+", "-", "/", "*"]
alphas = {}

def calc(A : float, B : float, op : str):
    if op == "+":
        return float(A + B)
    elif op == "-":
        return float(A - B)
    elif op == "*":
        return float(A * B)
    elif op == "/":
        return float(A / B)

n = int(input())
postfix = input().strip()

for i in range(n):
    alphas[chr(i + 65)] = float(input())

stx = []

for i in range(len(postfix)):
    if postfix[i] in oper:
        B = stx.pop()
        A = stx.pop()
        result = calc(A, B, postfix[i])
        stx.append(result)
    else:
        stx.append(alphas[postfix[i]])

print("{:.2f}".format(float("".join(map(str,stx)))))


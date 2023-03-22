# 분수의 덧셈
import math
def solution(denum1, num1, denum2, num2):
    # 분모의 최소공배수를 찾는다.
    num_lcm = (num1 * num2) // math.gcd(num1, num2)
    # 분자를 분모가 곱해진 값과 같게 맞추어준다.
    denum1 *= (num_lcm // num1)
    denum2 *= (num_lcm // num2)
    # 약분 해준다.
    # 분모 분자의 최대 공약수 찾기
    gcd = math.gcd(denum1 + denum2, num_lcm)
    answer = [(denum1 + denum2) // gcd, num_lcm // gcd]
    return answer

# 그냥 서로 곱해서 더하기
def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]
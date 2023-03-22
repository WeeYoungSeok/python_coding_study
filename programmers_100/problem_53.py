# 피자 나눠 먹기(2)
def solution(n):
    def gcd(a, b):
        if a % b == 0:
            return b
        return gcd(b, a % b)
    return (n * 6) // gcd(n, 6) // 6

# 다른 풀이
def solution1(n):
    i = 1
    while True:
        if (6 * i) % n == 0:
            return i
        i += 1
        
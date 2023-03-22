# list = [0, 1]
# def pibo(n):
#     for i in range(2, n + 1):
#         x = list[i - 2] + list[i - 1]
#         list.append(x)
#     return list[n]
# n = int(input())
# print(pibo(n))

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)
n = int(input())
print(fibo(n))

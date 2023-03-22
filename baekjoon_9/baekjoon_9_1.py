def pec(n):
    if n == 1 or n == 0:
        return 1
    return n * pec(n - 1)
  
n = int(input())
print(pec(n))
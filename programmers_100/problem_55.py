# 숫자 찾기
def solution(num, k):
    answer = str(num).find(str(k))
    return answer + 1 if answer != -1 else answer

# try except
def solution1(num, k):
    try:
      return str(num).index(str(k)) + 1
    except ValueError:
      return -1

# 삼항 연산자
def solution2(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1
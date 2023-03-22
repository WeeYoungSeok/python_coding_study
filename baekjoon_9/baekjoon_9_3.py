# one = "\"재귀함수가 뭔가요?\""
# two = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
# three = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
# four = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""

# def jh(n, count):
#     if n == 0:
#         return
#     if n == 1:
#         print("_" * count + one)
#         print("_" * count + '"재귀함수는 자기 자신을 호출하는 함수라네"')
#         print("_" * count + "라고 답변하였지.")
#         return
#     print("_" * count + one)
#     print("_" * count + two)
#     print("_" * count + three)
#     print("_" * count + four)
#     jh(n - 1, count + 4)
#     print("_" * count + "라고 답변하였지.")

# n = int(input())
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# print(one)
# print(two)
# print(three)
# print(four)
# jh(n, 4)
# print("라고 답변하였지.")

def jh(m):
    x = 4 * (n - m)
    under = "_" * x
    print(under + '"재귀함수가 뭔가요?"')

    if m == 0:
        print(under + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(under + "라고 답변하였지.")
        return
    print(under + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(under + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print(under + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    jh(m - 1)
    print(under + "라고 답변하였지.")

n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
jh(n)
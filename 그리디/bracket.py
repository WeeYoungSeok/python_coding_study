n = input().split("-")
result = 0

i = 0

while True:
    if "+" in n[i]:
        list = n[i].split("+")
        if i == 0:
            result += sum(map(int, list))
        else:
            result += - sum(map(int, list))
    else:
        if i == 0:
            result += int(n[i])
        else:
            result += - int(n[i])
    i += 1
    if i >= len(n):
        break

print(result)


# number = ""
# newN = ""
# for i in n:
#     if i != "+" and i != "-":
#         number += i
#     else:
#         newN += number.lstrip("0")
#         newN += i
#         number = ""
      
# newN += number.lstrip("0")

# flag = False
# i = 0
# while True:
#     if newN[i] == "-":
#         if flag == True:
#             newN = newN[:i] + ")" + newN[i:]
#             flag = False
#         else:
#             newN = newN[:i + 1] + "(" + newN[i + 1:]
#             flag = True
#     i += 1
#     if i == len(newN):
#         break
          
# if newN.find("(") != -1 and (newN[len(newN) - 1]) != ")":
#     newN = newN + ")"

# print(eval(newN))
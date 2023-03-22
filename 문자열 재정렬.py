# 문자열 재정렬

# words = input()

# word1 = 0
# word2 = []

# for word in words:
#     print(ord(word))
#     if ord(word) >= 49 and ord(word) <= 57:
#         word1 += int(word)
#     else:
#         word2.append(word)
# word2.sort()
# print(''.join(word2) + str(word1))

# 나동빈님 코드
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print("".join(result))
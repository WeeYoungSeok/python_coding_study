list = [
  "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"
]

word = input()
result = 0
for x in word:
    for i in range(1, len(list)):
        if x in list[i]:
            result += int(i) + 2

print(result)
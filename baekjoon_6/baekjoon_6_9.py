alpha = [
  "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="
]

word = input()
oldLen = len(word)
cro_count = 0

for i in alpha:
    if i in word:
        cro_count += word.count(i)
        word = word.replace(i, "-1" * len(i))
print(cro_count + oldLen - word.count("-1"))

alpha = [
  "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="
]

word = input()

for i in alpha:
    word = word.replace(i, "1")
print(len(word))
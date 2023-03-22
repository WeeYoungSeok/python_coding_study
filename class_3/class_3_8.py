import sys

input = sys.stdin.readline

m = int(input())

s = set()
for _ in range(m):
    word = input().strip()
    new_word = word.split(" ")
    if len(new_word) == 1:
        s = set()
        if new_word[0] == "all":
            for i in range(1, 21):
                s.add(i)
    else:
        new_word_alpha = new_word[0]
        new_word_number = int(new_word[1])
        if new_word_alpha == "add":
            # if new_word_number not in s:
            s.add(new_word_number)
        elif new_word_alpha == "remove":
            # if new_word_number in s:
            s.discard(new_word_number)
        elif new_word_alpha == "check":
            if new_word_number in s:
                print(1)
            else:
                print(0)
        else:
            if new_word_number in s:
                s.discard(new_word_number)
            else:
                s.add(new_word_number)
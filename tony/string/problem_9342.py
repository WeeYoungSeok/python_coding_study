# 염색체
# baekjoon 9342
# https://www.acmicpc.net/problem/9342

import sys


def input():
    return sys.stdin.readline()


t = int(input())

# A, B, C, D, E, F = 아스키 코드 65 ~ 70
# 그 이후 알파벳은 71 ~ 90


def A_F(s):
    if ord(s) >= 65 and ord(s) <= 70:
        return True
    else:
        return False


for _ in range(t):
    word = input().strip()
    # step 시작
    if len(word) < 3:
        print("Good")
        continue

    if A_F(word[0]) == False:
        print("Good")
        continue

    zero_a = False

    if word[0] != "A":
        if word[1] != "A":
            print("Good")
            continue
    else:
        zero_a = True

    start_a_i = 1 if zero_a == True else 2

    start_f_i = 0
    start_c_i = 0
    for i in range(start_a_i, len(word)):
        if word[i] != "A":
            start_f_i = i
            break

    if start_f_i == 0 or word[start_f_i] != "F":
        print("Good")
        continue

    for i in range(start_f_i, len(word)):
        if word[i] != "F":
            start_c_i = i
            break

    if start_c_i == 0 or word[start_c_i] != "C":
        print("Good")
        continue

    last_i = start_c_i
    for i in range(start_c_i, len(word)):
        if word[i] != "C":
            last_i = i
            break

    if last_i != start_c_i:
        if last_i + 1 != len(word):
            print("Good")
            continue
        else:
            if A_F(word[last_i]) == False:
                print("Good")
                continue

    print("Infected!")

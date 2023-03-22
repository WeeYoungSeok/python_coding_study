import sys

input = sys.stdin.readline

s = input().strip()
start = ord('a')
for i in range(start, ord(s) + 1):
    print(chr(i), end = " ")
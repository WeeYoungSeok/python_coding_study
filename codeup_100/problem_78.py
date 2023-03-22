import sys

input = sys.stdin.readline

while True:
    s = input().strip()
    if s == "q":
        print(s)
        break
    print(s)
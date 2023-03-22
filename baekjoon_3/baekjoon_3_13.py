import sys

while True:
    try:
        one, two = map(int, sys.stdin.readline().split())
        print(one + two)
    except:
        break
      
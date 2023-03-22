from collections import deque
import sys

input = sys.stdin.readline

def deqCheck(deq):
    if deq:
        return True
    else:
        return False
deq = deque()

n = int(input())

for _ in range(n):
    x = input().strip()
    if "push_front" in x:
        deq.appendleft(x.split()[1])
    elif "push_back" in x:
        deq.append(x.split()[1])
    elif x == "front":
        if deqCheck(deq) == True:
            print(deq[0])
        else:
            print("-1")
    elif x == "back":
        if deqCheck(deq) == True:
            print(deq[-1])
        else:
            print("-1")
    elif x == "size":
        print(len(deq))
    elif x == "empty":
        if deqCheck(deq) == True:
            print("0")
        else:
            print("1")
    elif x == "pop_front":
        if deqCheck(deq) == True:
            print(deq.popleft())
        else:
            print("-1")
    elif x == "pop_back":
        if deqCheck(deq) == True:
            print(deq.pop())
        else:
            print("-1")

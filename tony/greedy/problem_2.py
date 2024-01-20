# 민겸 수
from collections import deque

mks = list(input())

max_value = ''
min_value = ''

max_dq = deque()
min_dq = deque()

# max
for mk in mks:
    if mk == 'M':
        max_dq.append(mk)
        min_dq.append(mk)
    else:
        max_value += '5'
        while max_dq:
            max_dq.pop()
            max_value += '0'
        if min_dq:
            min_value += '1' + '0' * (len(min_dq) - 1)
            min_dq.clear()
        min_value += '5'

if max_dq:
    max_value += '1' * len(max_dq)

if min_dq:
    min_value += '1' + '0' * (len(min_dq) - 1)


print(max_value)
print(min_value)

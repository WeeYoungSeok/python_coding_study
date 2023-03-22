# 특이한 정렬
def solution(numlist, n):
    answer = []
    answer.append(numlist[0])
    del numlist[0]
    for i in range(len(numlist)):
        new_list = []
        for j in range(len(answer) - 1, -1, -1):
            if abs(n - answer[j]) > abs(n - numlist[i]):
                new_list.append(answer[j])
                del answer[j]
            elif abs(n - answer[j]) == abs(n - numlist[i]):
                if answer[j] < numlist[i]:
                    new_list.append(answer[j])
                del answer[j]
        answer = answer + new_list[::-1]
    return answer

# 람다 정렬식
# abs(x - n) 으로 가까운 값으로 먼저 정렬한 뒤
# 가까운 값이 같다면 해당 값이 큰 순서대로 정렬을 해야하니 n - x로 정렬하면 된다
# 이유는 정렬 람다에서 인자가 음수가 되면 내림차순인데 ex) n = 4 x = 2와 x = 6이라 가정할 때 n - x = 2 와 n - x = -2로 나오게 된다. 이 경우 음수로 판별돼 6이 앞에 오게 된다.
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer
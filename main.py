# import sys

# input = sys.stdin.readline

# N = int(input())

# x_i = list(map(int, input().split()))

# x_i_sort = sorted(list(set(x_i)))

# # 여기서 그냥 배열끼리 비교해서
# # 하면 index 시간 복잡도가 O(n)이라서 n^2이 된다
# # 이 문제 n이 100만까지이므로 100만 X 100만이 되어버림
# # for i in x_i:
#     # print(x_i_sort.index(i), end=" ")

# # 튜플로 만들면 찾는 시간 복잡도가
# # O(1)이므로 시간이 많이 줄어든다.
# dic = {x_i_sort[i] : i for i in range(len(x_i_sort))}
# for i in x_i:
#     print(dic[i], end=" ")

# items = ['1', '2', '3', '4']
# from itertools import permutations
# print(list(permutations(items, 4)))


def solution(n, words):
    answer = [0, 0]
    duple_words = []
    p = 1
    before_word = ""

    for word in words:
        # 중복을 말하거나 전 단어의 끝 알파벳을 시작으로 끝말잇기를 시작 안한다면 탈락
        if (word in duple_words) or (before_word != "" and before_word[len(before_word) - 1] != word[0]):
            answer[0] = p
            answer[1] += 1
            break

        # 말한 단어 중복 단어 체크를 위해 넣어둠
        duple_words.append(word)
        # 순번 증가
        p += 1
        # 만약 증가된 순번이 n보다 커진다면
        # 첫번째 사람으로 돌아옴
        if p > n:
            # 첫번째로 초기화
            p = 1
            # 한바퀴 돌았다는 의미
            answer[1] += 1

        # 현재 말한 단어를 다음 단어와 비교하기 위해 
        before_word = word

    # 만약 탈락한 사람이 없다면
    # 0, 0으로 리턴해야하기 때문에 바퀴수도 0으로 초기화
    if answer[0] == 0:
        answer[1] = 0
    return answer

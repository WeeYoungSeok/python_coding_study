# 영어 끝말잇기
def solution(n, words):
    answer = [0, 0]
    duple_words = []
    p = 1
    before_word = ""

    for word in words:
        # 중복을 말하거나 전 단어의 끝 알파벳을 시작으로 끝말잇기를 시작 안한다면 탈락
        if (word in duple_words) or (
                before_word != ""
                and before_word[len(before_word) - 1] != word[0]):
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

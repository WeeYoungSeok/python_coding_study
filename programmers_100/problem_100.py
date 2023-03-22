# 옹알이(1)
def solution(babbling):
    nephew_words = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for nephew_word in nephew_words:
            babbling[i] = babbling[i].replace(nephew_word, "-1")
    for i in range(len(babbling)):
         babbling[i] =  babbling[i].replace("-1", "")
    return babbling.count("")

# replace로 풀기
# replace로 ""로 치환하면 단어끼리 붙어서 발음이 되는 경우가 발생한다.
# 그것을 대비해 " " 공백으로 치환을해서 단어끼리 붙는 것을 막고 공백만 존재하면 발음이 가능한 단어이므로 strip()으로 공백을 지운 뒤 len을 검사하여 0인 경우 발음이 가능한 단어라로 판단한다.
def solution(babbling):
    answer = 0
    nephew_words = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for nephew_word in nephew_words:
            babbling[i] = babbling[i].replace(nephew_word, " ")
        if len(babbling[i].strip()) == 0:
            answer += 1
    return answer

# 둥수 매기기
def solution(score):
    answer = [0] * len(score)
    avg_list = []
    for avg in score:
        avg_list.append((avg[0] + avg[1]) / 2)
    avg_list.sort()
    rank_dict = {avg_list[0] : 1}
    del avg_list[0]
    for i in range(len(avg_list)):
        for key in list(rank_dict.keys()):
            avg = avg_list[i]
            if key < avg:
                rank_dict[key] += 1
                if avg not in rank_dict:
                     rank_dict[avg] = 1
    for key in list(rank_dict.keys()):
        for i in range(len(score)):
            if key == (score[i][0] + score[i][1]) / 2:
                answer[i] = rank_dict[key]
    return answer
  
# 다시 풀기
def solution(score):
    answer = []
    avg_list = []
    for avg in score:
        avg_list.append((avg[0] + avg[1]) / 2)
    avg_list.sort(reverse = True)
    rank_dict = {}
    for i in range(len(avg_list)):
        if avg_list[i] not in rank_dict.keys():
            rank_dict[avg_list[i]] = i + 1
    for s in score:
        answer.append(rank_dict[(s[0] + s[1]) / 2])
    return answer
  
# 다른 사람 풀이
def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    # i에는 인덱스 r에는 그 해당 인덱스의 값이 들어옴
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]
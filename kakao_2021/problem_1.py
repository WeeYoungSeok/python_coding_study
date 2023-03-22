# 숫자 문자열과 영단어
def solution(s):
    num_dict = {
      "one" : "1",
      "two" : "2",
      "three" : "3",
      "four" : "4",
      "five" : "5",
      "six" : "6",
      "seven" : "7",
      "eight" : "8",
      "nine" : "9",
      "zero" : "0"
    }
    # for key in list(num_dict.keys()):
    #     s = s.replcae(key, num_dict[key])
    for key, value in num_dict.items():
        s = s.replace(key, value)
    return int(s)

# 배열의 인덱스로 풀기
def solution(s):
    num_array = [
      "zero",
      "one",
      "two",
      "three",
      "four",
      "five",
      "six",
      "seven",
      "eight",
      "nine",]
    for i in range(len(num_array)):
        s = s.replace(num_array[i], str(i))
    return int(s)
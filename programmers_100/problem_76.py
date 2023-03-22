# 영어가 싫어요
def solution(numbers):
    num_dict = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    for key in num_dict.keys():
        numbers = numbers.replace(key, str(num_dict[key]))
    return int(numbers)

# 배열의 idx로 풀기
def solution(numbers):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in dic:
        numbers = numbers.replace(word, str(i))
        i+=1
    return int(numbers)
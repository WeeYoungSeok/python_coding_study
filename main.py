def solution(numbers, target):
    lst = [0]
    for num in numbers:
        temp = []
        for l in lst:
            temp.append(l + num)
            temp.append(l - num)
        lst = temp
        
    return lst.count(target)
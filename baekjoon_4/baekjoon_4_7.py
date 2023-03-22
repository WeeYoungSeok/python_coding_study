c = int(input())

for _ in range(c):
    student_score = list(map(int, input().split()))
    avg = sum(student_score[1:]) / student_score[0]
    count = 0
    for i in student_score[1:]:
        if i > avg:
            count += 1
    print("{:.3f}%".format(count / student_score[0] * 100))


# 나의 풀이
# c = int(input())

# for _ in range(c):
#     student_score = list(map(int, input().split()))
#     avg = sum(student_score[1:]) / student_score[0]  
#     over = [x for x in range(1, len(student_score)) if student_score[x] > avg]
#     print("{:.3f}%".format(len(over) / student_score[0] * 100))
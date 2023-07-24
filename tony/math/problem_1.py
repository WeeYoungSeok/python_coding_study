# 수

# 0 ~ 9까지 n개 뽑은 경우의 수
def gen_permutations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i, elem in enumerate(arr):
        for P in gen_permutations(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + P]

    return result


# 조합으로 나온 숫자들 [1, 2, 3] = int의 형태로 바꾸기
def arrToInt(arr):
    answer = ""
    for i in arr:
        answer += str(i)
    return int(answer)


# arr = gen_permutations([0, 1, 2], 2)

# for i in arr:
#     print(arrToInt(i))


# 0 ~ 9까지 k가지의 숫자를 한 번씩만 사용할 경우
# 1 <= k <= 5이므로 가장 큰 숫자는 98765
# 98765까지의 소수를 구한다.
# 에라토스테네스의 체
def primeList(n):
    # n을 포함시키기 위함
    n += 1
    # [False(0), False(1), True(2), True(3), True(4) ... True(n)]
    sieve = [False, False] + [True] * (n)
    end = int(n**0.5) + 1
    for i in range(2, end):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(n) if sieve[i] == True]


# 결과값
count = 0

k, m = map(int, input().split())

# 0 ~ 9까지 k개 뽑기
k_permutations = []
k_permutation = gen_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k)
for i in k_permutation:
    if i[0] != 0:
        k_permutations.append(i)
# print(k_permutations)

# 두가지를 만족하는 수인지 판별하기 위한 True False 배열
answer = [False] * (arrToInt(k_permutations[len(k_permutations) - 1]) + 1)

answer_2 = [False] * (arrToInt(k_permutations[len(k_permutations) - 1]) + 1)

prime_numbers = primeList(arrToInt(k_permutations[len(k_permutations) - 1]))

# step 1
for i in k_permutations:
    attach_i = arrToInt(i)
    for j in range(0, len(prime_numbers)):
        if prime_numbers[j] >= attach_i:
            break
        bool = False
        for k in range(j + 1, len(prime_numbers)):
            if prime_numbers[j] + prime_numbers[k] > attach_i:
                break
            elif prime_numbers[j] + prime_numbers[k] == attach_i:
                answer[attach_i] = True
                bool = True
                break
        if bool == True:
            break

# step 2
for i in k_permutations:
    attach_i = arrToInt(i)
    while attach_i % m == 0:
        attach_i /= m
    attach_i = int(attach_i)
    for j in range(0, len(prime_numbers)):
        if prime_numbers[j] >= attach_i:
            break
        if prime_numbers[j]**2 == attach_i:
            answer_2[attach_i] = True
            break
        bool = False
        for k in range(j + 1, len(prime_numbers)):
            if prime_numbers[j] * prime_numbers[k] > attach_i:
                break
            elif prime_numbers[j] * prime_numbers[k] == attach_i:
                answer_2[attach_i] = True
                bool = True
                break
        if bool == True:
            break

for i in range(0, len(answer)):
    if answer[i] == True and answer_2[i] == True:
        count += 1

print(count)





###############
# 다른 풀이
# 0 ~ 9까지 n개 뽑은 경우의 수
def gen_permutations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i, elem in enumerate(arr):
        for P in gen_permutations(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + P]

    return result


# 조합으로 나온 숫자들 [1, 2, 3] = int의 형태로 바꾸기
def arrToInt(arr):
    answer = ""
    for i in arr:
        answer += str(i)
    return int(answer)


# arr = gen_permutations([0, 1, 2], 2)

# for i in arr:
#     print(arrToInt(i))


# 0 ~ 9까지 k가지의 숫자를 한 번씩만 사용할 경우
# 1 <= k <= 5이므로 가장 큰 숫자는 98765
# 98765까지의 소수를 구한다.
# 에라토스테네스의 체
def primeList(n):
    # n을 포함시키기 위함
    n += 1
    # [False(0), False(1), True(2), True(3), True(4) ... True(n)]
    sieve = [False, False] + [True] * (n)
    end = int(n**0.5) + 1
    for i in range(2, end):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(n) if sieve[i] == True]

# 결과값
count = 0

k, m = map(int, input().split())

# 0 ~ 9까지 k개 뽑기
k_permutations = []
k_permutation = gen_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k)
for i in k_permutation:
    if i[0] != 0:
        k_permutations.append(i)

# 두가지를 만족하는 수인지 판별하기 위한 True False 배열
answer = [False] * (arrToInt(k_permutations[len(k_permutations) - 1]) + 1)
# print(answer)

answer_2 = [False] * (arrToInt(k_permutations[len(k_permutations) - 1]) + 1)
# print(answer_2)

temp = [i for i in range(1, arrToInt(k_permutations[len(k_permutations) - 1]) + 1)]
# print(temp)
for i in range(0, len(temp)):
    a = temp[i]
    while a % m == 0:
        a /= m
    temp[i] = int(a)
# print(temp)

prime_numbers = primeList(arrToInt(k_permutations[len(k_permutations) - 1]))

for j in range(0, len(prime_numbers)):
        bool = False
        for k in range(j + 1, len(prime_numbers)):
            if prime_numbers[j] + prime_numbers[k] > len(answer) - 1:
                break
            # print("에러 나기 전 : ", prime_numbers[j] + prime_numbers[k])
            answer[prime_numbers[j] + prime_numbers[k]] = True

for i in range(0, len(answer)):
    for j in range(0, len(prime_numbers)):
        same_number = prime_numbers[j] **2
        if same_number in temp:
            answer_2[same_number] = True
        for k in range(j + 1, len(prime_numbers)):
            diff_number = prime_numbers[j] * prime_numbers[k]
            if diff_number in temp:
                answer_2[diff_number] = True

for i in range(0, len(answer)):
    if answer[i] == True and answer_2[i] == True:
        count += 1

# print("결과")
# print(answer)
# print(answer_2)
print(count)


# 틀려서 다시 품
import itertools


# 조합으로 나온 숫자들 [1, 2, 3] = int의 형태로 바꾸기
def arrToInt(arr):
    answer = ""
    for i in arr:
        answer += str(i)
    return int(answer)



# 0 ~ 9까지 k가지의 숫자를 한 번씩만 사용할 경우
# 1 <= k <= 5이므로 가장 큰 숫자는 98765
# 98765까지의 소수를 구한다.
# 에라토스테네스의 체
def primeList(n):
    # n을 포함시키기 위함
    n += 1
    # [False(0), False(1), True(2), True(3), True(4) ... True(n)]
    sieve = [False, False] + [True] * (n)
    end = int(n**0.5) + 1
    for i in range(2, end):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(n) if sieve[i] == True]

# 결과값
count = 0

k, m = map(int, input().split())


# num_dic[int(''.join(map(str,i)))] = 0
# 0 ~ 9까지 k개 뽑기
k_permutations = []
k_permutation = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k))

# 처음에 0으로 시작하는 수 빼고 저장
for i in k_permutation:
    if i[0] != 0:
        k_permutations.append(int(''.join(map(str, i))))


# 두 조건을 만족하는 수를 담을 딕셔너리
num_dic = {}

# 소수
prime_numbers = primeList(k_permutations[len(k_permutations) - 1])

prime_dic = {}

for i in prime_numbers:
    prime_dic[i] = 0

# 소수를 돌면서 만약 두 합이 만족하는 소수가 소수라면 1조건이 만족하므로 num_dic에 추가
for j in range(0, len(prime_numbers)):
        for k in range(j + 1, len(prime_numbers)):
            if prime_numbers[j] + prime_numbers[k] in k_permutations:
                num_dic[prime_numbers[j] + prime_numbers[k]] = 0

# 두번째 조건
for i in num_dic:
		# m으로 나누어 떨어지지 않을때까지 나누어 준뒤
    a = i
    while a % m == 0:
        a /= m
		# 소수를 순회하면서
    for j in range(0, len(prime_numbers)):
						# 만약 제곱한 값이 a라면 추가
            same_number = prime_numbers[j] **2
            if same_number == a:
                if i in num_dic:
                    num_dic[i] += 1
                else:
                    num_dic[i] = 0
						# 다음 소수들을 순회하면서
            for k in range(j + 1, len(prime_numbers)):
								# 두개의 곱이 a와 같다면 추가
                diff_number = prime_numbers[j] * prime_numbers[k]
                if diff_number == a:
                    if i in num_dic:
                        num_dic[i] += 1
                    else:
                        num_dic[i] = 0

answer = 0
for key in num_dic:
    if num_dic[key] > 0:
        count += 1
print(count)

# 하지만 시간 초과



# 결국 코드 참고해서 다시품
# in 연산자를 사용할때는 dict, set을 쓰자
import itertools


# 조합으로 나온 숫자들 [1, 2, 3] = int의 형태로 바꾸기
def arrToInt(arr):
    answer = ""
    for i in arr:
        answer += str(i)
    return int(answer)



# 0 ~ 9까지 k가지의 숫자를 한 번씩만 사용할 경우
# 1 <= k <= 5이므로 가장 큰 숫자는 98765
# 98765까지의 소수를 구한다.
# 에라토스테네스의 체
def primeList(n):
    # n을 포함시키기 위함
    n += 1
    # [False(0), False(1), True(2), True(3), True(4) ... True(n)]
    sieve = [False, False] + [True] * (n)
    end = int(n**0.5) + 1
    for i in range(2, end):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(n) if sieve[i] == True]

# 결과값
count = 0

k, m = map(int, input().split())


# num_dic[int(''.join(map(str,i)))] = 0
# 0 ~ 9까지 k개 뽑기
k_permutations = []
k_permutation = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k))

for i in k_permutation:
    if i[0] != 0:
        k_permutations.append(int(''.join(map(str, i))))


num_dic = {}

prime_numbers = primeList(k_permutations[len(k_permutations) - 1])
prime_dic = {}

for i in prime_numbers:
    prime_dic[i] = 0

for i in k_permutations:
    for j in prime_dic:
        if i - j <= j:
            break
        if i - j in prime_dic:
            num_dic[i] = 0
            break

for i in num_dic:
    a = i
    while a % m == 0:
        a /= m
    for j in prime_dic:
            if j >= a:
                break
            if a // j in prime_dic and a % j == 0:
                if i in num_dic:
                    num_dic[i] += 1
                    break

answer = 0
for key in num_dic:
    if num_dic[key] > 0:
        count += 1
print(count)
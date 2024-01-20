# 행복 유치원

# 이해하기 상당히 빡세고
# 방법을 찾은 사람들이 대단할뿐이다..

# 내 머리로 이해한 부분은
# dndrldzk@gmail.com
# 메일에 넣어놨다 pdf로

# pdf보고
# 막대 1개 설치 (조 2개 편성)시에 왜 diff를 1개 (가장 큰 값) 빼고 다 더해주는거지? 의문을 또 가질까봐 미래의 나에게 남기는 메세지

# 가장 큰 막대가 사라지는건 알지?
# 왜냐고? 가장 크게 차이 나는 애들은 찢어놔야 되거든 그래야 돼 안그러면 무조건 그거보다 크게 나와 니가 여러번 해봐 다시 

# 이해하기 쉽게 설명하자면
# 찢는 순간 가장 큰 값 - 가장 작은 값이잖아?
# 그러면 가장 큰 값 - 가장 작은 값은
# diff에서 구해놓은 애들 다 더한거랑 같은거잖아 
# 그니깐 가장 큰 값을 찢어야 한다고 
# 가장 큰 값 안찢으면 결국 가장 큰 값도 diff에서 더해줘야 되니깐 숫자 개커진다고 빡대가리야 ㅇㅋ?

# 결국 막대 설치하는 곳이 가장 큰 값이고 그 큰 값은 막대 개수만큼 diff에서 제외시키는거임 

# 가장 큰 값 - 가장 작은 값
# 가장 작은 값의 인덱스부터 인접한 바로 옆 값의 차들의 합(가장 큰 값까지)
# 이걸 기억하셈
# 식도 있어 pdf에 다시 곱씹어봐

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
st = list(map(int, input().split()))
diff = []

for i in range(n - 1):
    diff.append(st[i + 1] - st[i])

# 내림차순 정렬시
diff.sort(reverse=True)

print(sum(diff[k - 1:n - 1]))

# 오름차순 정렬시
diff.sort()

print(sum(diff[0:n - k]))
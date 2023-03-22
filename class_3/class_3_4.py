# 비밀번호 찾기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

site_array = {}
find_array = []
for i in range(n + m):
    if i > n - 1:
        find_array.append(input().strip())
    else:
        site_pw = input().strip().split()
        site_array[site_pw[0]] = site_pw[1]

for find_site in find_array:
    if find_site in site_array:
        print(site_array[find_site])
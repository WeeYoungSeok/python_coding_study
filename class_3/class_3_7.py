from collections import deque

def virus_check(graph, start, visited):
    if len(graph[start]) == 0:
        return
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
          
n = int(input())
m = int(input())

array = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    f, e = map(int, input().split())
    array[f].append(e)
    array[e].append(f)

virus_check(array, 1, visited)

print(visited.count(True) - 1 if visited.count(True) > 1 else 0)
import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    count = 1
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and graph[ny][nx] == 1:
                count += 1
                visited[ny][nx] = True
                deq.append((ny, nx))
    return count


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
visited = [[False for _ in range(m)] for j in range(n)]
deq = deque()
dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)
counts = []
answer = [0, 0]

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            visited[i][j] = True
            deq.append((i, j))
            counts.append(bfs())

if len(counts) == 0:
    print(0)
    print(0)
else:
    print(len(counts),max(counts),sep="\n")
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while deq:
        yy, xx = deq.popleft()
        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if 0 <= ny < y and 0 <= nx < x and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                graph[ny][nx] = graph[yy][xx] + 1
                deq.append((ny, nx))


y, x = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(y)]
visited = [[False for _ in range(x)] for _ in range(y)]
dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)
deq = deque()
visited[0][0] = True
deq.append((0, 0))

bfs()
print(graph[y-1][x-1])
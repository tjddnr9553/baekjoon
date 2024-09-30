import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(a)]
flag = True

for y in range(a):
    if graph[b - 1][c - 1] < graph[y][c - 1]:
        flag = False

for x in range(a):
    if graph[b - 1][c - 1] < graph[b - 1][x]:
        flag = False

if flag:
    print("HAPPY")
else:
    print("ANGRY")

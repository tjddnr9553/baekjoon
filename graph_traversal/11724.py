import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(num):
    if visited[num]:
        return
    visited[num] = True

    for j in arr[num]:
        if not visited[j]:
            dfs(j)


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)

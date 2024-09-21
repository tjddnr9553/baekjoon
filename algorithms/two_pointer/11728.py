import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = []
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_idx, b_idx = 0, 0

for _ in range(n + m):
    if a_idx == n and b_idx != m:
        for i in b_list[b_idx:]:
            answer.append(i)
        break
    elif a_idx != n and b_idx == m:
        for i in a_list[a_idx:]:
            answer.append(i)
        break

    if a_idx != n or b_idx != m:
        if a_list[a_idx] < b_list[b_idx]:
            answer.append(a_list[a_idx])
            a_idx += 1
        else:
            answer.append(b_list[b_idx])
            b_idx += 1
print(*answer, end="")

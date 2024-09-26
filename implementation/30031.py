import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    if 142 > a >= 136:
        answer += 1000
    elif 148 > a >= 142:
        answer += 5000
    elif 154 > a >= 148:
        answer += 10000
    elif a >= 154:
        answer += 50000

print(answer)

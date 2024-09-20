import sys

input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))
init_data = sum(arr[0:0 + x])
visitor = [init_data]

for i in range(1, n - x + 1):
    visitor.append(visitor[i-1] - arr[i - 1] + arr[i + x - 1])

if max(visitor) == 0:
    print("SAD")
else:
    print(max(visitor), visitor.count(max(visitor)), sep="\n")

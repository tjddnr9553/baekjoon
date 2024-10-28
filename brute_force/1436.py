import sys
input = sys.stdin.readline

n = int(input())
num = 0
count = 0
while count != n:
    if "666" in str(num):
        count += 1
    num += 1

print(num-1)
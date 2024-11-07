arr = [0 for _ in range(3)]
for i in range(len(arr)):
    arr[i] = int(input())

print(int(arr[1]/arr[0]*arr[2]))
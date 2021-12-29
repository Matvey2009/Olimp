N = int(input())
arr = list(map(int, input().split()))
k = 0

for i in range(N):
    if 437 >= arr[i]:
        k += 1
if k <= 0:
    print('No crash')
else:
    print('Crash', k)
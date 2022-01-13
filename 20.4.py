N = int(input())
arr = [0] * ((N-1) // 2)
T = int(input())
for i in range(T):
    K, S = map(int, input().split())
    arr[K-1] = (arr[K-1] + S) % ((N-1) * 4 - (K-1) * 8)

matrix = [0] * N
for i in range(N):
    matrix[i] = [1] * N

for i in range(len(arr)):
    tN = N - i * 2
    L = (tN - 1) * 4
    for x in range(tN):
         matrix[i][i + x] = (x - arr[i]) % L + 1
         matrix[N - i - 1][i + x] = (L - (tN - 2) - x - arr[i] - 1) % L + 1
    for y in range(tN-2):
        matrix[y + i + 1][i] = (L - y - arr[i] - 1) % L + 1
        matrix[y + i + 1][N - i - 1] = (tN + y - arr[i]) % L + 1

for i in matrix:
    print(*i)
    
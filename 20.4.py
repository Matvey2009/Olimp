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
        matrix[i][(N - tN) // 2 + x] = x+1
        #Низ#
        pass
    for y in range(N):
        #Лево#
        #Прав#
        pass

for i in matrix:
    print(*i)
    
N = int(input())
A = list(map(int, input().split()))
K = int(input())
g = 0
c = 0

for i in range(N):
    if A[i] < 0:
        g += 1
        if A[i] < c:
            c = A[i]
if g <= K:
    print(g)
else:
    print(g)
    print(abs(c))
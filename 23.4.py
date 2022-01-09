N = list(input().split())
N.sort()

for i in range(317, 1000):
    q = i*i
    res = list(str(q))
    res.sort()
    if res == N:
        print(q)
        break
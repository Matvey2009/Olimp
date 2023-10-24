n = int(input())
m = int(input())
k = int(input())
c = int(input())
s = 0
for i in range(n):
    temparr = list()
    for j in range(m):
        temparr.append((i*n+j)%k+1)
    s += temparr.count(c)
print(s)

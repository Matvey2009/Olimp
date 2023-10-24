n = int(input())
k = int(input())
s = n//k+k
if n%k ==0:
    s-=1
print(s)

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
s = 0

for i in range(q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        arr[(line[1] - 1 + s) % n] = line[2]
    else:
        s = (s - arr[i]) % n
    print(sum(arr))
    
    
#temp = [0] * n
#for j in range(n):
#    temp[j] = arr[(j - line[1]) % n]
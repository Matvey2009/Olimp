n = int(input())
arrm = []
arrs = []
arrb = []
arr = list(map(int, input().split()))
arr.sort()
t1 = t2 = n//2
if (n & 1):
	t2 += 1
else:
	t1 += 1
for i in range(t1):
	arrm.append(arr[i])
arr.reverse()
for i in range(t2):
	arrb.append(arr[i]) 
for i in range(n//2):
	arrs.append(arrb[i])
	arrs.append(arrm[i])
if (n & 1):
	if (t2 > t1):
		arrs.append(arrb[t1])
	else:
		arrs.append(arrm[t2])
print(*arrs)


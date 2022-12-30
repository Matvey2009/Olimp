n = int(input())
arr = list(map(int, input().split()))
s = 0
for k in range(n):
	s += (k+1) * arr[k]
m = s
for i in range(n):
	for j in range(i+1, n):
		t = s - arr[i]*i - arr[j]*j + arr[i]*j + arr[j]*i
		m = max(t, m)
print(m)




#s = 0
#n = int(input())
#arr = list(map(int, input().split()))
#for k in range(n):
#	s += (k+1) * arr[k]
#for i in range(n):
#	for j in range(i+1, n):
#		arr[i], arr[j] = arr[j], arr[i]
#		temp = 0
#		for k in range(n):
#			temp += (k+1) * arr[k]S
#		arr[j], arr[i] = arr[i], arr[j]
#		s = max(s, temp)
#print(s)

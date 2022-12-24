s = 0
n = int(input())
arr = list(map(int, input().split()))
for k in range(n):
	s += (k+1) * arr[k]
for i in range(n):
	for j in range(i+1, n):
		arr[i], arr[j] = arr[j], arr[i]
		temp = 0
		for k in range(n):
			temp += (k+1) * arr[k]
		arr[j], arr[i] = arr[i], arr[j]
		s = max(s, temp)
print(s)

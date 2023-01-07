n = int(input())
arr = list(map(int, input().split()))
k = m = sum(arr)
a = 0
for i in range(n):
	a += arr[i]
	m = min(abs(a-(k-a)) , m)
print(m)

t = int(input())
for i in range(t):
	s = 0
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort(reverse=True)
	for i in range(2, n, 3):
		s += arr[i]
	print(s)

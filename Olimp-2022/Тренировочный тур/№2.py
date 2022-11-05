t = int(input())
for i in range(t):
	n = int(input())
	k = round(n**(1.0/3.0))
	if (k**3 == n):
		print('YES')
	else:
		print('NO')

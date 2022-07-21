t = int(input())
for i in range(t):
	n = int(input())
	shops = list(map(int, input().split()))
	print((max(shops) - min(shops))*2)

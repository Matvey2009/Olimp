n = int(input())
arr = list(map(int, input().split()))

temp = 0
for i in range(len(arr)):
	temp, arr[i] = arr[i], arr[i] - temp

t = int(input())
for i in range(t):
	l, r, v = map(int, input().split())
	arr[l-1] += v
	if (r < n):
		arr[r] -= v

temp = 0
for i in range(len(arr)):
	arr[i] += temp
	temp = arr[i]
print(*arr)


#n = int(input())
#arr = list(map(int, input().split()))
#t = int(input())
#for i in range(t):
#	l, r, v = map(int, input().split())
#	for j in range(l-1, r):
#		arr[j] += v
#print(*arr)

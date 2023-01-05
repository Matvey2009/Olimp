n = int(input())
s = 0
d = 100
arr = []
for i in range(n):
	arr.append(list(input()))
	d = min(d, len(arr[i]))
for i in range(d):
	temp = arr[0][i]
	for j in range(n):
		if arr[j][i] != temp:
			temp = -1
			break
	if temp == -1:
		break
	s+=1
print(s)

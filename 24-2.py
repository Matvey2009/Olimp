arr = []
for i in range(3):
	for j in input().split():
		arr.append(int(j))
for i in range(9):
	for j in range(i+1, 9):
		arr[i], arr[j] = arr[j], arr[i]
		if (sum(arr[0:3])==sum(arr[3:6])==sum(arr[6:9])==sum(arr[0:7:3])==sum(arr[1:8:3])==sum(arr[2:9:3])):
			break
		else:
			arr[j], arr[i] = arr[i], arr[j]
for i in range(0, 9, 3):
	print(arr[i], arr[i+1], arr[i+2])

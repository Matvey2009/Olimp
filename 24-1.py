arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
p1 = p2 = 0

for i in range(3):
	if arr1[i] > arr2[i]:
		p1 += 1
	elif arr2[i] > arr1[i]:
		p2 += 1
if p1 > 1:
	print(1)
elif p2 > 1:
	print(2)
else:
	print(0)

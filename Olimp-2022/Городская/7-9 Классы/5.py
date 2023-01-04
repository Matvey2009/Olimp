arr = list(input())
lmini = lmaxi = pmini = pmaxi = 0
for i in range(3):
	if (arr[i] == "*"):
		lmaxi += 9
	else:
		lmini += int(arr[i])
		lmaxi += int(arr[i])
		
	if (arr[i+3] == "*"):
		pmaxi += 9
	else:
		pmini += int(arr[i+3])
		pmaxi += int(arr[i+3])
if (lmaxi >= pmini and pmaxi >= lmini):
	print("Yes")
else:
	print("No")

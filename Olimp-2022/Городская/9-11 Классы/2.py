arr1 = list(input())
arr2 = list(input())
arrtemp = []
arr1 = list(set(arr1))
arr2 = list(set(arr2))
for i in range(len(arr1)):
	if (arr1[i] in arr2 and arr1[i] not in arrtemp):
		arrtemp.append(arr1[i])
if (len(arrtemp) == 0):
	print('epidemic')
else:
	arrtemp.sort()
	print (''.join(arrtemp))

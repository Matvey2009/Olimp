n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
k = int(input())
arrtest = []
arr1.sort()
arr2.sort()
x = k - min(k, len(arr1))
arr1 = arr1[:min(k, len(arr1))]
arr2 = arr2[:min(k+x, len(arr2))]

for i in range(len(arr1)):
	for j in range(len(arr2)):
		arrtest.append(arr1[i] + arr2[j])
arrtest.sort()

print(arrtest[k-1])


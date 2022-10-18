a, b = input().split()
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
darr = []
for i in range(26):
	if(a == arr[i]):
		x = i
	if(b == arr[i]):
		y = i
	
for i in range(26):
	if(i >= x and i <= y):
		darr.append(arr[i])


print("Позиция 'a' - ", x)
print("Позиция 'b' - ", y)
print(*darr)

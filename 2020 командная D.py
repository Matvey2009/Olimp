n = int(input())
countmaxi = 0
count = 0
prev = 0
for i in map(int, input().split()):
	if i > prev: #Некрасивый строй
		count = 1
	else:		 #Красивый строй
		count += 1
	if (count > countmaxi):
		countmaxi = count
	prev = i
	#print(i, count)
print(countmaxi)

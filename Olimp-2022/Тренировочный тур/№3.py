n, m = map(int, input().split())
st = r = 0
arr = []
for i in range(n):
	s = list(map(int, input().split()))
	arr.append(s)
	temp = 1e10
	for j in range(m):
		if (s[j] < temp):
			temp = s[j]
			ty = i
	if (temp > st):
		st = temp
		y = ty
for j in range(m):
	if (arr[y][j] == st):
		for i in range(n):
			if (arr[i][j] > st):
				break
			if (i == n-1):
				r = str(st)+'\n'+str(y)+' '+str(j)
				break
print(r)


	









#n, m = map(int, input().split())
#st = 0
#arr = []
#conPos = []
#con = []
#for i in range(n):
#	arr.append(list(map(int, input().split())))
#for i in range(len(arr)):
#	temp = 1e10
#	tempPos = []
#	for j in range(len(arr[i])):
#		if (arr[i][j] < temp):
#			temp = arr[i][j]
#			tempPos = [i, j]
#	con.append(temp)
#	conPos.append(tempPos)
#for i in range(len(con)):
#	st = max(st, con[i])
#for i in range(len(conPos)):
#	if (arr[conPos[i][0]][conPos[i][1]] == st):
#		stPos = conPos[i]
#		break
#print(st)
#print(*stPos)

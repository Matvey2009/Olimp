n, m = map(int, input().split())
x, y = map(int, input().split())
x -= 1
y -= 1
k = int(input())
arr = dict()
res = "SUCCESS"
for i in range(k):
	a, b, c = input().split()
	a, b = int(a)-1, int(b)-1
	if a not in arr.keys():
		arr[a] = dict()
	if a in arr.keys() and b not in arr[a]:
		arr[a][b] = []
	if a in arr.keys() and b in arr[a] and c not in arr[a][b]:
		arr[a][b].append(c)
	if c == "U" and a-1 >= 0:
		c = "D"
		a -= 1
	elif c == "L" and b-1 >= 0:
		c = "R"
		b -= 1
	elif c == "R" and b+1 < m:
		c = "L"
		b += 1
	elif c == "D" and a+1 < n:
		c = "U"
		a += 1
	if a not in arr.keys():
		arr[a] = dict()
	if a in arr.keys() and b not in arr[a]:
		arr[a][b] = []
	if a in arr.keys() and b in arr[a] and c not in arr[a][b]:
		arr[a][b].append(c)
for i in input():
	if x in arr.keys() and y in arr[x].keys() and i in arr[x][y]:
		res = "FAIL"
		break
	if i == "U":
		x -= 1
	elif i == "D":
		x += 1
	elif i == "L":
		y -= 1
	elif i == "R":
		y += 1
	if x < 0 or x >= n or y >= m or y < 0:
		res = "FAIL"
		break
print(res)




















#Превышин лимит времени
#n, m = map(int, input().split())
#x, y = map(int, input().split())
#x -= 1
#y -= 1
#k = int(input())
#arr = []
#res = "SUCCESS"
#for i in range(k):
#	a, b, c = input().split()
#	a, b = int(a)-1, int(b)-1
#	abc = [a, b, c]
#	if abs not in arr:
#		arr.append(abc)	 
#	if c == "U" and a-1 >= 0:
#		c = "D"
#		a -= 1
#	elif c == "L" and b-1 >= 0:
#		c = "R"
#		b -= 1
#	elif c == "R" and b+1 < m:
#		c = "L"
#		b += 1
#	elif c == "D" and a+1 < n:
#		c = "U"
#		a += 1
#	abc = [a, b, c]
#	if abs not in arr:
#		arr.append(abc)	 
#for i in input():
#	for abc in arr:
#		if x == abc[0] and y == abc[1] and i == abc[2]:
#			res = "FAIL"
#			break
#	if i == "U":
#		x -= 1
#	elif i == "D":
#		x += 1
#	elif i == "L":
#		y -= 1
#	elif i == "R":
#		y += 1
#	if x < 0 or x >= n or y >= m or y < 0:
#		res = "FAIL"
#		break
#print(res)




#Превышен лимит памяти
#n, m = map(int, input().split())
#x, y = map(int, input().split())
#x -= 1
#y -= 1
#k = int(input())
#arr = [[[] for j in range(m)] for i in range(n)] 
#res = "SUCCESS"
#for i in range(k):
#	a, b, c = input().split()
#	a, b = int(a)-1, int(b)-1
#	if c not in arr[a][b]:
#		arr[a][b].append(c)
#	if c == "U" and a-1 >= 0:
#		c = "D"
#		a -= 1
#	elif c == "L" and b-1 >= 0:
#		c = "R"
#		b -= 1
#	elif c == "R" and b+1 < m:
#		c = "L"
#		b += 1
#	elif c == "D" and a+1 < n:
#		c = "U"
#		a += 1
#	if c not in arr[a][b]:
#		arr[a][b].append(c)
#for i in input():
#	for j in arr[x][y]:
#		if j == i:
#			res = "FAIL"
#			break
#	if res == "FAIL":
#		break
#	if i == "U":
#		x -= 1
#	elif i == "D":
#		x += 1
#	elif i == "L":
#		y -= 1
#	elif i == "R":
#		y += 1
#	if x < 0 or x >= n or y >= m or y < 0:
#		res = "FAIL"
#		break
#print(res)



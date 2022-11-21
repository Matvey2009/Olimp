n, m = map(int, input().split())
x, y = map(int, input().split())
x,y = x-1, y-1
arr = [[[] for j in range(m)] for i in range(n)] 
res = "SUCCESS"
for i in range(int(input())):
	a, b, c = input().split()
	a, b = int(a)-1, int(b)-1
	if c not in arr[a][b]:
		arr[a][b].append(c)
	if arr[a][b] == "U" and a-1 >= 0:
		c = "D"
		a -= 1
	elif arr[a][b] == "D" and a+1 >= 0:
		c = "U"
		a += 1
	elif arr[a][b] == "R" and b+1 <= 0:
		c = "L"
		b += 1
	elif b-1 <= 0:
		c = "R"
		b -= 1
	if c not in arr[a][b]:
		arr[a][b].append(c)
		
for i in input():
	if i in arr[x][y]:
		res = "FAIL"
		break
	if i == "U":
		y += 1
	elif i == "D":
		y -= 1
	elif i == "L":
		x -= 1
	else:
		x += 1
	if x < 0 or x >= n or y >= m or y < 0:
		res = "FAIL"
		break
print(res)


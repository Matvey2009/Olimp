n, m = map(int, input().split())
x, y = map(int, input().split())
x -= 1
y -= 1
k = int(input())
arr = [[[] for j in range(m)] for i in range(n)] 
res = "SUCCESS"
for i in range(k):
	a, b, c = input().split()
	a, b = int(a)-1, int(b)-1
	if c not in arr[a][b]:
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
	if c not in arr[a][b]:
		arr[a][b].append(c)
for i in input():
	for j in arr[x][y]:
		if j == i:
			res = "FAIL"
			break
	if res == "FAIL":
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


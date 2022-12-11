a, b = map(int, input().split())
if (min(a, b) + 1 >= max(a, b)):
	c = -1
else:
	c = min(a, b)+1
print(c)

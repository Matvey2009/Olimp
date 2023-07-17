a, b = map(int, input().split())
s = min(a % b, b - a % b)
for i in range(s):
	bp = b+i
	bm = b-i
	s = min(s, a % bp + i, a % bm + i, bp - a % bp + i, bm - a % bm + i)
print(s)

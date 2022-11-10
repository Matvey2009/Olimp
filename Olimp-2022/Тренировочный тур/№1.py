for i in range(int(input())):
	l, r = map(int, input().split())
	l, r = l-l%2, r+r%2
	print((r**2-l**2)//4)



#t = int(input())
#for i in range(t):
#	l, r = map(int, input().split())
#	s = 0
#	for j in range(l, r+1):
#		if (j % 2 != 0):
#			s += j
#	print(s)

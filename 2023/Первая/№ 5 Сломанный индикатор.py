p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = 0
arr = list()
n = int(input())
for i in range(n):
	x = int(input())
	if x == 0:
		p1 = p2 = p4 = p6 = p8 = p9 = 1 #0
	elif x == 1:
		p3 = p4 = p8 = 1 #1
	elif x == 2:
		p1 = p4 = p7 = p9 = 1 #2
	elif x == 3:
		p1 = p3 = p5 = p7 = 1 #3
	elif x == 4:
		p2 = p4 = p5 = p8 = 1 #4
	elif x == 5:
		p1 = p2 = p5 = p8 = p9 = 1 #5
	elif x == 6:
		p3 = p5 = p6 = p8 = p9 = 1 #6
	elif x == 7:
		p1 = p3 = p6 = 1 #7
	elif x == 8:
		p1 = p2 = p4 = p5 = p6 = p8 = p9 = 1 #8
	elif x == 9:
		p1 = p2 = p4 = p5 = p7 = 1 #9
if p1 == 1 and p2 == 1 and p4 == 1 and p6 == 1 and p8 == 1 and p9 == 1: #0
	print(0)
if p3 == 1 and p4 == 1 and p8 == 1: #1
	print(1)
if p1 == 1 and p4 == 1 and p7 == 1 and p9 == 1: #2
	print(2)
if p1 == 1 and p3 == 1 and p5 == 1 and p7 == 1: #3
	print(3)
if p2 == 1 and p4 == 1 and p5 == 1 and p8 == 1: #4
	print(4)
if p1 == 1 and p2 == 1 and p5 == 1 and p8 == 1 and p9 == 1: #5
	print(5)
if p3 == 1 and p5 == 1 and p6 == 1 and p8 == 1 and p9 == 1: #6
	print(6)
if p1 == 1 and p3 == 1 and p6 == 1: #7
	print(7)
if p1 == 1 and p2 == 1 and p4 == 1 and p5 == 1 and p6 == 1 and p8 == 1 and p9 == 1: #8
	print(8)
if p1 == 1 and p2 == 1 and p4 == 1 and p5 == 1 and p7 == 1: #9
	print(9)


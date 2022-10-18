a, b, c, d = map(int, input().split())
x = str(a+b+c+d)
if(int(x[-1:]) == 1 and int(x[-1:]) != 11):
	print(x, "птица")
elif(int(x[-1:]) >= 2 and int(x[-1:]) <= 4 and int(x) != 14 and int(x) != 13 and int(x) != 12):
	print(x, "птицы")
else:
	print(x, "птиц")

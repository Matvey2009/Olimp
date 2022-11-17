s = '-' + '-'.join(input()) + '-'
d = len(s)
arr = [0]*d
maxi = c = r = 0
for i in range(d):
	j = 0 if (i > c+r) else min(arr[c-(i-c)], c+r-i)
	while i-j>0 and i+j<d-1 and s[i-j-1] == s[i+j+1]:
		j += 1 
	if (i+j > c+r):
		c,r = i,j
	arr[i]=j
	maxi = max(maxi, j)
print(maxi)




#s = '-' + '-'.join(input()) + '-'
#d = len(s)
#maxi = 0
#for i in range(d):
#	temp = -1
#	for j in range(min(i, d-i-1)+1):
#		if (s[i-j] == s[i+j]):
#			temp += 1
#			maxi = max(temp, maxi)
#		else:
#			break
#print(maxi)







#s = input()
#maxi = 0
#for i in range(len(s)):
#	for j in range(i, len(s)):
#		test = s[i:j+1]
#		if (test == test[::-1]):
#			maxi = max(len(test), maxi)
#print(maxi)
			


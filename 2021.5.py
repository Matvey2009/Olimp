S = input()
maxi = 0
for i in range(len(S)):
    for j in range(i, len(S)):
        test = S[i:j+1]
        if test == test[::-1]:
            if len(test) > maxi:
                maxi = len(test)
print(maxi)
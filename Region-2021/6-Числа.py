x = input()
k = input()

if k == '0':
    n = x[0]
    for i in x:
        if i == n:
            continue
        elif i > n:
            n = str(int(n) + 1)
            break
        else:
            break
    print(n*len(x))

else:
#   for i in x:
#        x = i-1
#        if x != i:
#            1W 
    print(0)
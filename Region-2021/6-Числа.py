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
    while True:
        if max(x.count(x[0]), x.count(x[-1])) < len(x)-1:
            x = str(int(x) + 1)
        else:
            break
    print(x)
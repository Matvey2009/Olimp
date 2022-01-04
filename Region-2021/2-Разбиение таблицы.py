t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    k = n * m
    s = int((1 + k) * k / 2)
    ps= s / 2
    v =  m // 2
    col1 = (1 + (n-1) * m + 1) * n / 2
    colv = (v + (n-1) * m + v) * n / 2
    colv2= ((v+1) + (n-1) * m + (v+1)) * n / 2
    vs  = (col1 + colv)  * v / 2
    vs2 = (col1 + colv2) * (v+1) / 2
    vr = abs(ps - vs )
    vr2= abs(ps - vs2)
    
    if vr <= vr2:
        minV = vr
        col  = v
    else:
        minV = vr2
        col  = v+1

    h   = round(n * 0.70666667) #Доделать#
    hs  = (1 + h*m) * h*m / 2
    hs2 = (1 + (h+1)*m) * (h+1)*m / 2
    hr = abs(ps - hs )
    hr2= abs(ps - hs2)
    
    if hr <= hr2:
        minH = hr
        row  = h
    else:
        minH = hr2
        row  = h+1
    
    if minV <= minH:
        print('V', col+1)
    else:
        print('H', row+1)
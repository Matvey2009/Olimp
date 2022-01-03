t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    k = n * m
    s = int((1 + k) * k / 2) ; print('Вся сумма:', s) #Удалить#
    ps = s / 2 ; print('Половина всей суммы:', ps)
    v =  m // 2
    col1 = (1 + (n-1) * m + 1) * n / 2 ; print('Первая  колонка:', col1)
    colv = (v + (n-1) * m + v) * n / 2 ; print('Средняя колонка:', colv)
    vs = (col1 + colv) * v / 2 ; print('Сумма левой половины', vs)
    vr = ps - vs ; print('Отклонение левой половины', vr)
    vr2= ps - (s - vs) ; print('Отклонение правой половины', vr2)
    
    row1 = ((1 + (m+1) * n - 1) * m / 2) / m ; print('Первый ряд', row1)
    rowv = ((m / 2) + (1 + (m+1) * n - 1) * m / 2) - k ; print('Второй ряд', row2)
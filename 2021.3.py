N, M = map(int, input().split())
arr  = []


for y in range(N):
    arr.append(list(map(int, input().split())))

maxY = posY = posY = tmpX = 0
for y in range(N):
    minX = 1000000000
    for x in range(M):
        if arr[y][x] < minX:
            minX = arr[y][x]
            tmpX = x
    if minX > maxY:
        maxY = minX
        posY = y
        posX = tmpX

for y in range(N):
    if maxY < arr[y][posX]:
        maxY = 0
        break
        
print(maxY)
if maxY > 0:
    print(posY, posX)

#Cедловая точка- это максимальный элемент в строке и минимальный в столбце
#5 4
#2 3 2 5
#1 2 1 3
#9 8 5 6
#3 4 3 4
#2 1 2 3
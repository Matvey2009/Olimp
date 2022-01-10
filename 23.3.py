P = int(input())
maxi =  9999999999 #10**9#
mini = -9999999999 #10**9#

for i in range(P):
    N = input()
    if N[-1:] == '>':
        temp = int(N[:-1])
        if temp < maxi:
            maxi = temp
    if N[-1:] == '<':
        temp = int(N[:-1])
        if temp > mini:
            mini = temp
print(max(maxi, mini) - min(maxi, mini))
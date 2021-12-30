d, m, w = map(int, input().split())
i, j, k = map(int, input().split())
print(chr(ord('a') + ((k-1)*m*d + (j-1)*d + (i-1)) %w))
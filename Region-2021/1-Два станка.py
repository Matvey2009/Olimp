k = int(input())
a, x = map(int, input().split())
b, y = map(int, input().split())
print(max(max(k-a, 0)*x + max(k-a-b, 0)*y, max(k-b, 0)*y + max(k-b-a, 0)*x))
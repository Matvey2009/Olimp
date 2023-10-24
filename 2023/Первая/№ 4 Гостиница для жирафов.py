n = int(input())
numbers = list()
result = 0
while result < n:
    mini = min(n - result, result + 1)
    numbers.append(mini)
    result += mini
print(*numbers)

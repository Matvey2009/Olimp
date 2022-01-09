S, A, B = map(int, input().split())
if (S % A) == (S % B):
    print(0)
elif (S % A) < (S % B):
    print(1)
else:
    print(2)
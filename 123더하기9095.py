def pl(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return pl(n-1) + pl(n-2) + pl(n-3)
    
test = int(input())

for num in range(test):
    x = pl(int(input()))
    print(x)

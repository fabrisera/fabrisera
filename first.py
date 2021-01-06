a = list(input().split())
n = int(a[0])
s = int(a[1])

while s > 0:
    if n % 10 == 0:
        n = n / 10
    else:
        n -= 1
    s -= 1    
print(int(n))            

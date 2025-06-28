n = 3846739
soluong = 0
a = []
while ( n > 0):
    soluong += 1
    n = n / 10
for i in range(1,soluong):
    a[i] = n % 10
    n = n / 10
tong = 0
for i in range(soluong,1,-1):
    tong += a[i] * 10
print(tong)
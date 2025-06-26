n = 3846739
soluong = 0
a = []
while ( n > 0):
    soluong += 1
    n = n/10
for i in range(1,soluong):
    a[i] = n % 10
tong = 0
for i in range(2,soluong):
    if a[i-1] > a[i] & a[i] < a[i+1]:
        print("cuc tieu la ",a[i])
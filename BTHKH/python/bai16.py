n = 3846739
soluong = 0
while ( n > 0):
    soluong += 1
    n = n/10
for i in range(0,soluong):
    if ( i > (i+1) ) :
        print("các chữ số không tăng dần")
    if ( i < (i+1) ) :
        continue
        if ( (soluong-1) < soluong ):
            print("các chữ số tăng dần")



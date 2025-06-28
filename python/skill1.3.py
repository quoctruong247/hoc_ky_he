#Giái phương trình bậc 2 ax^2 + bx + c =0 , a, b, c nhập từ bàn phím.
a=float(input("nhap a:"))
b=float(input("nhap b:"))
c=float(input("nhap c:"))
if a==0:
    if b==0 and c==0:
        print("phuong trinh vo so nghiem")
    elif b==0 and c!=0:
        print("phuong trinh vo nghiem")
    else:
        x=-c/b
        print("nghiem phuong trinh la: ",x)
else:
    delta=b**2-4*a*c

    if delta < 0:
        print("phuong trinh vo nghiem")
    elif delta==0:
        x=-b / (2*a)
        print("phuong trinh co nghiem kep:",x)
    else:
        x1= (-b + math.sqrt(delta)) / (2*a)
        x2= (-b - math.sqrt(delta)) / (2*a)
        print("phuong trinh coa hai nghiem phan biet: ")
        print("x1",x1)
        print("x2",x2)
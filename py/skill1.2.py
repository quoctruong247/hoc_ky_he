#Giải phương trình bậc nhất ax + b=0, a, b được nhập từ bàn phím.
a=float(input("nhap a:"))
b=float(input("nhap b:"))
if a==0 and b==0:
    print("phuong trinh vo so nghiem")
elif a==0 and b!=0:
    print("phuong trinh vo nghiem")
else:
    x=-b/a
    print("nghiem phuong trinh la: ",x)
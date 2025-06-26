#1. Viết chương trình nhập vào một số, kiểm tra số đó có phải là số chẵn hay không? (chỉ dùng if)
n=int(input("nhap vao mot so :"))
if n%2==0:
    print("day la so chan")
else:
    print("day la so le")
if n>0:
    print("day la so duong")
elif n<0:
    print("day la so am")
else:
    print("khong phai so duong va am")



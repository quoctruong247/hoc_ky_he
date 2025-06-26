def hello():
    print("Hello")
def add(num1,num2):
    return num1+num2
#1.Viet ham ktr so nguyen to
def ktr_SNT(num):
    if num < 2:
        return False
    else:
        for i in range(2, num-1):
            if num%i==0:
                return False
    return True
#2.Viet ham ktr so chinh phuong
def ktr_SCP(num):
    if num >0:
        for i in range(1,int(num/2)+2):
            if i*i==num:
                return True
    return False
#3.Viet ham ktr so hoan thien
def ktr_SHT(num):
    tong=0;
    if num>0:
        for i in range(1,num-1):
            if num%i==0:
                tong+=i
    return tong==num
if __name__== '__main__':
    hello()
    #f-> , bth thi +
    print(f"Gia tri",add(1,2))
    num=eval(input("Nhap so ban muon ktr: "))
    if ktr_SNT(num):
        print(num, f" la so nguyen to")
    else:
        print(num, f" khong la so nguyen to")
    if ktr_SCP(num):
        print(num, f" la so chinh phuong")
    else:
        print(num, f" khong la so chinh phuong")
    if ktr_SHT(num):
        print(num, f" la so hoan thien")
    else:
        print(num, f" khong la so hoan thien")


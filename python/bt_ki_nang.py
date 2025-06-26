import math

def tongCS(num):
    tong1 = 0
    while num:
        tong1 += int(num % 10)
        num = int(num / 10)
    return tong1
def tongCSChan(num):
    tong2 = 0
    while num:
        if int(num % 10) % 2 == 0:
            tong2 += int(num % 10)
        num = int(num / 10)
    return tong2
def tongCSLe(num):
    tong3 = 0
    while num:
        if int(num % 10) % 2 == 1:
            tong3 += int(num % 10)
        num = int(num / 10)
    return tong3
def tongCSChiaHet2(num):
    tong4 = 0
    while num:
        if int(num % 10) % 2 == 0:
            tong4 += int(num % 10)
        num = int(num / 10)
    return tong4
def tongCSLaUoc8(num):
    tong5=0
    while num:
        if int(num % 10)%8==0:
            tong5+=int(num % 10)
        num=int(num / 10)
    return tong5
def ktr_CSTangDan(num):
    while num:
        numtemp=int(num % 10)
        num=int(num / 10)
        if(int(num % 10))>numtemp:
            return False
    return True
def ktr_CSGiamDan(num):
    while num:
        numtemp=int(num % 10)
        num=int(num / 10)
        if(int(num % 10))<numtemp:
            return False
    return True
def CSMax(num):
    Mnum=int(num%10)
    while num:
        num=int(num / 10)
        if (int(num % 10))>Mnum:
            Mnum=int(num % 10)
    return Mnum
def tongCT(num):
    numl=numtemp=tong9=0
    while num:
        numl = int(num % 10)
        num=int(num / 10)
        numtemp=int(num % 10)
        num=int(num / 10)
        if int(num % 10)<numtemp>numl or int(num % 10)>numtemp<numl:
            tong9+=numtemp
    return tong9
def tongCTieu(num):
    numl = numtemp = tong10 = 0
    while num:
        numl = int(num % 10)
        num = int(num / 10)
        numtemp = int(num % 10)
        num = int(num / 10)
        if int(num % 10) > numtemp < numl:
            tong10 += numtemp
    return tong10
def tongCD(num):
    numl = numtemp = tong11 = 0
    while num:
        numl = int(num % 10)
        num = int(num / 10)
        numtemp = int(num % 10)
        num = int(num / 10)
        if int(num % 10) < numtemp > numl:
            tong11 += numtemp
    return tong11
def nghichDao(num):
    nNum=0
    i=1
    while num:
        nNum=nNum*(math.pow(10,i))+int(num%10)
        num=int(num / 10)
        i+=1
    return nNum
if __name__ == '__main__':
    # print("1.Nhap hai so a, b: ")
    # # Eval tac dung?
    # a = eval(input("Nhap a: "))
    # b = eval(input("Nhap b: "))
    # # Khong dung string + double duoc! -> f,
    # print(f"Phan nguyen cua hai so vua nhap la: ", a / b)
    # print(f"Phan du cua hai so vua nhap la: ", a % b)
    # print("2.Nhap 4 so nguyen a, b, c, d: ")
    # a1 = eval(input("Nhap a: "))
    # a2 = eval(input("Nhap b: "))
    # a3 = eval(input("Nhap c: "))
    # a4 = eval(input("Nhap d: "))
    # print(f"Trung binh cong cua 4 so vua nhap la: ", (a1 + a2 + a3 + a4) * 1.0 / 4)
    # print("3.Nhap gio, phut, giay: ")
    # h = eval(input("Nhap gio: "))
    # m = eval(input("Nhap phut: "))
    # s = eval(input("Nhap giay: "))
    # print(f"Tong gio phut giay vua nhap la: ", (h * 3600 + m * 60 * s))
    # print("4.Nhap n co 2 chu so: ")
    # n = int(input("Nhap n co 2 chu so: "))
    # #so sau -0 thi se bi loi division by zero...
    # print(f"Tong gia tri nguyen va du cua so vua nhap la: ", (int(n / 10) / int(n % 10) + int(n / 10) % int(n % 10)))
    # if n % 2 == 0:
    #     print(f"5.", n, f" la so chan")
    # else:
    #     print(f"5.", n, " la so le")
    # if (int(n / 10) / int(n % 10) + int(n / 10) % int(n % 10)) > 10:
    #     print(f"6.", n, f" co tong nguyen du lon hon 10")
    # else:
    #     print(f"6.", n, f" khong co tong nguyen du lon hon 10")
    # if (int(n / 10) - int(n % 10)) < 0:
    #     print(f"7.", n, f" co hieu 2 chu so nho hon 0")
    # else:
    #     print(f"7.", n, f" co hieu 2 chu so khong nho hon 0")
    # if int(n / 10) == int(n % 10):
    #     print(f"8.", n, f" co 2 chu so doi xung")
    # else:
    #     print(f"8.", n, f" co 2 chu so khong doi xung")
    # if int(n / 10) > int(n % 10):
    #     print(f"9.Chu so lon nhat cua ", n, f" la: ", int(n / 10))
    # else:
    #     print(f"9.Chu so lon nhat cua ", n, f"la: ", int(n % 10))
    # print(f"10.Chu so nghich dao cua n la: ", int(n % 10) * 10 + int(n / 10))
    # if int(n / 10) > int(n % 10):
    #     print(f"11.Chu so tang dan cua ", n, f" la: ", int(n / 10), "\t", int(n % 10))
    # else:
    #     print(f"11.Chu so tang dan cua ", n, f" la: ", int(n % 10), "\t", int(n / 10))
    # if int(n / 10) < int(n % 10):
    #     print(f"11.Chu so giam dan cua ", n, f" la: ", int(n / 10), "\t", int(n % 10))
    # else:
    #     print(f"11.Chu so giam dan cua ", n, f" la: ", int(n % 10), "\t", int(n / 10))
    # print("13.Nhap cac 2 tham so a, b cho pt bac nhat: ")
    # a0 = eval(input("Nhap a: "))
    # b0 = eval(input("Nhap b: "))
    # if a0 == 0:
    #     if b0 == 0:
    #         print(f"Pt ", a0, "x+", b0, f"=0 co vo so nghiem!")
    #     else:
    #         print(f"Pt ", a0, "x+", b0, f"=0 vo nghiem!")
    # else:
    #     print(f"Nghiem cua pt ", a0, "x+", b0, f"=0 la: ", -b0 / a0)
    # print("14.Nhap 3 tham so a, b, c cho pt bac hai sau: ")
    # a14 = eval(input("Nhap a: "))
    # b14 = eval(input("Nhap b: "))
    # c14 = eval(input("Nhap c: "))
    # delta = b14 * b14 - 4 * a14 * c14
    # if a14 == 0:
    #     if b14 == 0:
    #         if c14 == 0:
    #             print(f"Pt ", a14, "x^2+", b14, "x+", c14, "=0 co vo so nghiem!")
    #         else:
    #             print(f"Pt ", a14, "x^2+", b14, "x+", c14, "=0 vo nghiem!")
    #     else:
    #         print(f"Pt ", a14, "x^2+", b14, "x+", c14, "=0 co nghiem la: ", -c14 / b14)
    # else:
    #     if delta < 0:
    #         print(f"Pt ", a14, "x^2+", b14, "x+", c14, "=0 vo nghiem!")
    #     else:
    #         if delta > 0:
    #             print(f"Pt ", a14, "x^2+", b14, "x+", c14, "=0 co hai nghiem pb: x1=",
    #                   (-b14 + math.sqrt(delta) / 2 * a14), " va x2=", (-b14 + math.sqrt(delta) / 2 * a14))
    #         else:
    #             print(f"Pt ", a14, "x^2+", b14, "x+", c14, "=0 co nghiem kep: ", -b14 / 2 * a14)
    # # BT KY NANG 2
    # print("\nBAI TAP KY NANG 2")
    # if n > 0:
    #     print("1.", n, f" la mot so duong")
    # if n < 0:
    #     print("1.", n, f" la mot so am")
    # dtb = eval(input("Nhap diem trung binh: "))
    # print("\nCach 1: Chi dung if")
    # if 8.0 <= dtb <= 10.0:
    #     print("Loai gioi")
    # if 6.5 <= dtb < 8.0:
    #     print("Loai kha")
    # if 5.0 <= dtb <= 6.5:
    #     print("Loai trung binh")
    # if 3.5 <= dtb <= 5.0:
    #     print("Loai yeu")
    # if 0 <= dtb <= 3.5:
    #     print("Loai kem")
    # print("\nCach 2: Dung if else")
    # print("\nCach 3: Dung toan tu 3 ngoi")
    # sum4 = 0
    # for i in range(1, n,2):
    #     sum4 += i
    # print(f"4.Tong cac so le tu 1-n: ", sum4)
    # count5 = 0
    # for i in range(1, n,2):
    #     count5 += 1
    # print(f"5.Dem cac so le tu 1-n: ", count5)
    # count6 = 0
    # for i in range(1, n):
    #     if n % i == 0:
    #         count6 += 1
    # print(f"6.Dem cac uoc so cua n: ", count6)
    # sum7 = 0
    # for i in range(1, n):
    #     if n % i == 0:
    #         sum7 += i
    # print(f"7.Tong cac uoc so cua n tu 1-n: ", sum7)
    # count8 = 0
    # for i in range(6, n):
    #     if n % i == 0:
    #         count8 += 1
    # print(f"8.Dem cac uoc so lon hon 5 tu 1-n: ", count8)
    # count9 = 0
    # for i in range(1, n):
    #     if (i % 3 == 0) or (i % 2 == 0):
    #         count9 += 1
    # print(f"9.Dem cac so chia het cho 2 hoac 3: ", count9)
    # count10 = 0
    # for i in range(1, n):
    #     if (i % 3 == 0) and (i % 2 == 0):
    #         count10 += 1
    # print(f"10.Dem cac so chia het cho 2 va 3: ", count10)
    num = int(input("Nhap n co nhieu chu so: "))
    print(f"1.Tong cac chu so cua n: ",tongCS(num))
    print(f"2.Tong cac chu so chan cua n: ", tongCSChan(num))
    print(f"3.Tong cac chu so le cua n: ", tongCSLe(num))
    print(f"4.Tong cac chu so chia het cho 2 cua n: ",tongCSChiaHet2(num))
    print(f"5.Tong cac chu so la uoc cua 8 cua n: ",tongCSLaUoc8(num))
    if ktr_CSTangDan(num):
        print(f"6.",num," co cac chu so tang dan!")
    else:
        print(f"6.",num," khong co cac chu so tang dan!")
    if ktr_CSGiamDan(num):
        print(f"7.",num," co cac chu so giam dan!")
    else:
        print(f"7.",num," khong co cac chu so giam dan!")
    print(f"8.Chu so lon nhat cua n la: ",CSMax(num))
    print(f"9.Tong cac cuc tri cua n la: ",tongCT(num))
    print(f"10.Tong cac cuc tieu cua n la: ",tongCTieu(num))
    print(f"11.Tong cac cuc dai cua n la: ",tongCD(num))
    print(f"12.Nghich dao cac chu so cua n la: ",nghichDao(num))
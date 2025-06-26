if __name__ == '__main__':
    while True:
        gio = eval(input("Nhap gio: "))
        phut = eval(input("Nhap phut: "))
        giay = eval(input("Nhap giay: "))

        if gio>=0 and gio <=24 and phut >=0 and phut <=60 and giay >=0 and giay <=60:
            break
        print("Nhap sai! Nhap lai: ")
    sum = gio+phut+giay
    print(f"Tong la: ",sum)


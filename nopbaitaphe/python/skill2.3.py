#Viết chương trình nhập vào điểm trung bình, in ra xếp loại ( dùng 3 cách )
#8.0<= dtb <= 10.0 : giỏi
#6.5 <= dtb <8.0 : khá
#5.0 <= dtb < 6.5 : trung bình
#3.5 <= dtb < 5.0 : yếu
#0 <= dtb < 3.5 : kém
dtb= float(input("nhap diem trung binh: "))

if 8.0 <= dtb <=10:
    print("Xếp loại: Giỏi")
elif 6.5 <= dtb < 8.0:
    print("Xếp loại: Khá")
elif 5.0 <= dtb < 6.5:
    print("Xếp loại: Trung bình")
elif 3.5 <= dtb < 5.0:
    print("Xếp loại: Yếu")
elif 0 <= dtb < 3.5:
    print("Xếp loại: Kém")
else:
    print("diem nhap khong hop le")


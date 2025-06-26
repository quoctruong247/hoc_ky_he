dtb= float(input("nhap diem trung binh: "))
if dtb >= 8.0 and dtb <= 10.0:
    print("Xếp loại: Giỏi")
elif dtb >= 6.5 and dtb < 8.0:
    print("Xếp loại: Khá")
elif dtb >= 5.0 and dtb < 6.5:
    print("Xếp loại: Trung bình")
elif dtb >= 3.5 and dtb < 5.0:
    print("Xếp loại: Yếu")
elif dtb >= 0 and dtb < 3.5:
    print("Xếp loại: Kém")
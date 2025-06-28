
dtb= float(input("nhap diem trung binh: "))
muc_xep_loai = [
    (8.0, "Giỏi"),
    (6.5, "Khá"),
    (5.0, "Trung bình"),
    (3.5, "Yếu"),
    (0.0, "Kém")
]

for threshold, rank in muc_xep_loai:
    if dtb >= threshold:
        print(f"Xếp loại: {rank}")
        break
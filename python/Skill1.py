if __name__ =='__main__':
   #Nhập vào 2 số a,b in ra giá trị nguyên và giá trị dư của a, b.
    a = float(input("nhap vao gia tri cua a: "))
    b = float(input("nhap vao gia tri cua b: "))
    if b==0:
        print("khong the chia cho 0")
    phan_nguyen= a // b
    print(f"phan nguyen la: ",phan_nguyen)
    phan_du= a % b
    print(f"phan du la: ",phan_du)

    #Nhập vào 4 số nguyên a,b,c,d. tính trung bình cộng của 4 số đó.
    c = int(input("nhap so nguyen a: "))
    d = int(input("nhap so nguyen b: "))
    e = int(input("nhap so nguyen c: "))
    f = int(input("nhap so nguyen d: "))
    diem_trb= (c+d+e+f)/4
    print(f"trung binh cong la: ",diem_trb)
    #Nhập vào giờ phút giây, xuất ra màn hình giá trị tổng của giờ phút giây.
    gio = int(input("nhap so gio:"))
    phut = int(input("nhap so phut"))
    giay = int(input("nhap so giay"))
    tong_h_m_s = gio * 3600 + phut * 60 + giay
    print("tong so giay la:", tong_h_m_s)
   #Nhập vào n có 2 chữ số, tính tổng của giá trị phần nguyên và phần dư của n.
g = float(input("nhap vao so hai chu so: "))
Nguyen = int(g)
Du = g- Nguyen
tong=Nguyen+Du
print("phan nguyen: ",Nguyen)
print("phan du: ",Du)
print("tong: ",tong)
#Nhập vào n có 2 chữ số. kiểm tra n có số chẵn hay không?
e=float(input("nhap vao hai chu so: "))
if e % 2 == 0:
 print("day la so chan")
else:
 print("khong la so chan")
#Nhập vào n có 2 chữ số, kiểm tra n có tổng của phần nguyên và phần dư lớn hơn 10 hay không?
f = float(input("nhap vao hai chu so kiem tra:"))
Phan_nguyen=int(f)
Phan_du=f-Phan_nguyen
Tong_nguyen_du=Phan_nguyen+Phan_du
if Tong_nguyen_du > 10:
 print("day la so co nguyen du lon hon 10",Tong_nguyen_du)
else:
 print("day la so khong co tong lon hon 10")
#Nhập vào n có 2 chữ số, kiểm tra n có tổng của phần nguyên và phần dư lớn hơn 10 hay không?
h = float(input("nhap vao hai chu so kiem tra hieu co nho hon 0 hay khong: "))
if not (10<= abs(g) <=99):
 print("vui long nhap dung hai chu so")
else:
 hang_chuc = abs(h)//10
 hang_don_vi= abs(h)%10
 hieu=hang_chuc-hang_don_vi
 print("hieu=",hieu)
 if hieu < 0:
  print("hieu nho hon 0")
 elif hieu > 0:
  print("hieu lon hon 0")
#Nhập vào n có 2 chữ số, kiểm tra 2 số của n có đối xứng hay không?
j=float(input("nhap vao hai chu so: "))
chu_so_hc=j//10
chu_so_hdv=j%10
if chu_so_hc==chu_so_hdv:
 print("day la so doi xung")
else:
 print("day khong la so doi xung")
#Nhập vào n có 2 chữ số, in ra số lớn nhất
k=float(input("nhap vao hai chu so"))
Chu_so_hangc=k//10
Chu_so_hangdv=k%10
if Chu_so_hangc > Chu_so_hangdv:
 print("so lon nhat trong hai so la",Chu_so_hangc)
elif Chu_so_hangc < Chu_so_hangdv:
 print("so lon nhat trong hai so la",Chu_so_hangdv)
#Nhập vào n có 2 chữ số, xuất ra màn hình nghịch đảo của 2 số đó
l=float(input("nhap hai chu so:"))
phan_chuc=l//10
phan_dv=l%10
dao=phan_dv * 10 + phan_chuc
if l<0:
 dao=-dao
print("so dao la: ",dao)
#Nhập vào n có 2 chữ số, xuất ra màn hình thứ tự các chữ số tăng dần.
z=float(input("nhap so de xap xep"))
phan_Chuc=z//10
phan_Dv=z%10
so=[phan_Chuc,phan_Dv]
so_tang=sort(so)
print("thu tu tang dan ",so_tang[0],so_tang[1])
so_giam=sorted(so, reverse=True)
print("thu tu giam dan",so_giam[0],so_giam[1])


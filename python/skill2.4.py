n=int(input("nhap so nguyen n: "))
tong_le=0
for i in range(1,n+1):
    if i % 2 !=0:
        tong_le +=i
print("tong le: ",tong_le)
dem_so_le=0
for i in range(1,n+1):
    if i % 2 != 0:
        dem_so_le +=1
print("so luong so le la:",dem_so_le)
dem_uoc=0
for i in range(1,n+1):
    if n % i == 0:
        dem_uoc += 1
print("so luong cac uoc",dem_uoc)
tong_cac_uoc=0
for i in range(1,n+1):
    if n % i == 0:
        tong_cac_uoc += i
print("tong cac uoc",tong_cac_uoc)
dem_uoc_lon_hon_5=0
for i in range(1,n+1):
    if n % i == 0:
        if i>5:
            dem_uoc_lon_hon_5 += 1
print("cac uoc lon hon 5:",dem_uoc_lon_hon_5)
dem_chia_het_cho_2_or_3=0
for i in range(1,n+1):
    if i%2==0 or i%3==0:
        dem_chia_het_cho_2_or_3 +=1
print("cac so chia het cho 2,3 la",dem_chia_het_cho_2_or_3)
dem_chia_het_cho_2_va_3=0
for i in range(1,n+1):
    if i%2==0 and i%3==0:
        dem_chia_het_cho_2_va_3 +=1
print("cac so chia het cho 2,3 la",dem_chia_het_cho_2_va_3)

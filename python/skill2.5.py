n=int(input("nhap mot day so n:"))

tong=0
for i in range(1,n+1):
    chu_so= n%10
    tong+=chu_so
    n//=10
print("tong",tong)


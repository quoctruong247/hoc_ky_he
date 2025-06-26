#Class rỗng
class Person:
    #pass-->rong???In ra gi?
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def getName(self):
        return  self.name
    def getAge(self):
        return  self.age
#1.Tao lop PhanSo co tuSo va mauSo, nhap PhanSo va xuat PhanSo
class PhanSo:
    #self~=con tro this!
    def __init__(self,tuSo,mauSo):
        self.tuSo=tuSo
        self.mauSo=mauSo
    def get_tuSo(self):
        return self.tuSo
    def get_mauSo(self):
        return self.mauSo
    def get_PhanSo(self):
        return self.tuSo,self.mauSo
#2.Tao mot danh sach PhanSo, nhap va xuat ds PhanSo ra man hinh
class DSPS:
    def __init__(self,sl,PhanSo):
        self.sl=sl
        self.PhanSo=PhanSo
    def get_Stt(self):
        return self.sl

if __name__=='__main__':
    #Example
    p1 = Person("John",18)
    print(p1.getName(),p1.getAge())
    #Ex1:
    ps1 = PhanSo(1,3)
    print(ps1.get_tuSo(),ps1.get_mauSo())
    #Ex2:

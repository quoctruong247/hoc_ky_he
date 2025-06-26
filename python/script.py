def hello():
    print("Hello")
#nhap vao ktr 1 so chan hay le
def EvenOdd(number):
    if number%2==0:
        print("So Chan")
    else:
        print("So Le")
#xep loai (<3.5: kem, <5.0: Yeu, <6.5: TB, <8.0: Kha, <10: Gioi)
#def XepLoai(diem):


if __name__== '__main__':
    # print("Hello")
    # name=eval(input("What is your name?"))
    # if name>0:
    #     print(f'Hello,{name}')
    # if name >0:
    #     print("So Duong")
    # else:
    #      print("So Am")
    #
    # if name > 0:
    #     print("So Duong")
    # if not name >0:
    #     print("So Am")
    # hello()
    # number = eval(input("What is the number that you want to check?"))
    # EvenOdd(number)
    #multi assignment!
    age, gender, salary=20, True, 1000
    print(age, gender, salary)
    lan=hung=linh=17
    print(lan,hung,linh)
    #all th string --them eval ->int
    ten=input('Vui long nhap ten')
    #print((pow,ten))-- Khong duoc!
    #Thay the chuoi %s ->s%
    # s="%s la giao vien %s truong %s"
    # print(s%("Truong", "So Tu", "STU"))
    # s1="%s co tuoi la %d"
    # print(s1%("Truong", 45))
    # s2="Truong"
    # print(f"Hello,{s2}")
    # s0="Truong"
    # print(s0+"la giao vien cua truong")
    #list
    item1="apple"
    item2="banana"
    item3="cherry"

    shopping_list=["apple","banana","cherry"]
    print(shopping_list)
    print(shopping_list[0])
    print(shopping_list[1])
    print(shopping_list[2])
    shopping_list.append("blueberry")
    print(shopping_list)
    shopping_list[0]="red apple"
    print(shopping_list)
    del shopping_list[0]
    print(shopping_list)
    print(len(shopping_list))
    shopping_list1=["Hello","hi","biebie"]
    print(shopping_list+shopping_list1)
    print(shopping_list*2)
    #Khac c++ (mang gia tri limited) -> python la con tro
    list1= [2,3,4,5,6]
    print(list1)
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])
    print(list1[4])
    print(f"Gia tri max la =", max(list1))
    print(f"Gia tri min la =", min(list1))
    #dictionary

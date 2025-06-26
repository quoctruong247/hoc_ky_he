if __name__== '__main__':
    tuple1=(2,3,5,1,6,8)
    tuple2=(5,4,3,9,7,8)
    print(tuple1)
    print(len(tuple1))
    print("-------------check tuples")
    #xuat 2 3 5, 3 dai dien so phan tu xuat ra thoi!
    print(tuple1[0:3])
    print(tuple1[2:3])
    #xuat 5 1 6
    print(tuple1[2:-1])
    print(tuple1[2:-2])
    #Bo di so cuoi
    print(tuple1[:-1])
    #Lay lai so bi bo phia tren
    print(tuple1[-1:])
    print("---------print all tuples")
    print(tuple1+tuple2)
    for item in tuple1:
        print(item)
    print("-------------loop")
    for i in range(0,len(tuple1)):
        print(tuple1[i])
    print("\n")
    #So buoc tang 2
    for i in range(0, len(tuple1),2):
        print(tuple1[i])
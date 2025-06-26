if __name__ == '__main__':
    num = eval(input("Nhap a co 2 chu so: "))

    a = num // 10
    b = num % 10


    if a == b:
        print(f"2 chu so cua",num,"doi xung")
    else:
        print(f"2 chu so cua",num,"khong doi xung")

if __name__ == '__main__':
    num = eval(input("Nhap a co 2 chu so: "))

    a = num // 10
    b = num % 10

    minus = a - b
    if minus  < 0:
        print(f"Hieu 2 chu so cua",num,"bang",minus,"va nho hon 0")
    else:
        print(f"Hieeu 2 chu so cua",num,"bang",minus,"va khong nho hon 0")

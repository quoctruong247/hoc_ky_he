if __name__ == '__main__':
    num = eval(input("Nhap a co 2 chu so: "))

    a = num // 10
    b = num % 10

    sum = a +b
    if sum > 10:
        print(f"Tong 2 chu so cua",num,"bang",sum,"va lon hon 10")
    else:
        print(f"Tong 2 chu so cua",num,"bang",sum,"va khong lon hon 10")

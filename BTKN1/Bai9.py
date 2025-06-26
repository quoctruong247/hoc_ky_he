if __name__ == '__main__':
    num = eval(input("Nhap a co 2 chu so: "))

    a = num // 10
    b = num % 10

    if a > b:
        print(f"Chu so lon nhat cua", num, "la",a)
    elif a < b:
        print(f"Chu so lon nhat cua", num, "la",b)
    else:
        print(f"Hai chu so cua",num,"bang nhau")

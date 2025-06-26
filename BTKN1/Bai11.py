if __name__ == '__main__':
    num = eval(input("Nhap a co 2 chu so: "))

    a = num // 10
    b = num % 10

    if a < b:
        print(f"Thu tu tang dan la {a},{b}")
    else:
        print(f"Thu tu tang dan la {b},{a}")
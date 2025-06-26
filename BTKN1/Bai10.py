if __name__ == '__main__':
    num = eval(input("Nhap a co 2 chu so: "))

    a = num // 10
    b = num % 10
    print(f"So nghich dao cua {num} la {b*10 + a}")
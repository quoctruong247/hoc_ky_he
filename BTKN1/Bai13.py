if __name__ == '__main__':
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))

    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -b / a
        print(f"Nghiệm của phương trình là x = {round(x, 2)}")
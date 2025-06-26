if __name__ == '__main__':
    a = eval(input("Nhập a: "))
    b = eval(input("Nhập b: "))
    if b != 0:
        thuong = a // b
        du = a % b

        print("Thương nguyên:", thuong)
        print(f"Số dư: {du:.2f}")
    else:
        print("Không thể chia cho 0!")
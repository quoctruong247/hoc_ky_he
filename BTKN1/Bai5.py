from distutils.core import extension_keywords

if __name__ == '__main__':
    num = eval(input("Nhap a co 2 chu so: "))

    a = num // 10
    b = num % 10
    if a%2 ==0 and b%2 ==0:
        print(f"2 chu so cua",num,"deu chan")
    else:
        print(f"2 chu so cua",num,"khong cung chan")

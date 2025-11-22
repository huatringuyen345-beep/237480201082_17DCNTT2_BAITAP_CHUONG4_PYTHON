def chuoi(str):
    chu_hoa = 0
    chu_thuong  =0
    chu_so =0
    khac = 0
    for i in str:
        if i.isupper():
            chu_hoa += 1
        elif i.islower():
            chu_thuong += 1
        elif i.isdigit():
            chu_so += 1
        else:
            khac += 1

    print("===== KẾT QUẢ =====")
    print(f"Số chữ hoa: {chu_hoa}")
    print(f"Số chữ thường: {chu_thuong}")
    print(f"Số chữ số: {chu_so}")
    print(f"Ký tự khác: {khac}")

if __name__ == '__main__':
    while True:
        try:
            str = input(" Nhập vào chuỗi ký tự :")
            break
        except ValueError:
            print(" Đã xãy ra một ngoại lê !!!")
    chuoi(str)
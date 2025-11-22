def chuoi(str):
    tong =0
    for i in str:
        if i.isdigit():
            tong += int(i)
    print(f"Tổng  = {tong}")
if __name__ == "__main__":
    while True:
        try:
            str = input(" Nhập vào chuỗi ký tự :")
            break
        except ValueError:
            print(" Đã xãy ra một ngoại lê !!!")
    chuoi(str)
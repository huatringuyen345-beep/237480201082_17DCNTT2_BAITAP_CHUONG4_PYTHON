def gia_tri_xa_nhat(L, x):
    """Trả về giá trị trong L có khoảng cách xa x nhất."""
    max_kc = -1
    gia_tri = None

    for value in L:
        khoang_cach = abs(value - x)
        if khoang_cach > max_kc:
            max_kc = khoang_cach
            gia_tri = value

    return gia_tri


if __name__ == '__main__':

    while True:
        try:
            n = int(input("Nhập n: "))
            break
        except ValueError:
            print("Nhập số bất kỳ!")

    L = []
    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhập phần tử thứ {i+1}: "))
                L.append(x)
                break
            except ValueError:
                print("Nhập số nguyên hợp lệ!")

    while True:
        try:
            x = int(input("Nhập giá trị x: "))
            break
        except ValueError:
            print("Nhập số bất kỳ!")

    # Gọi hàm
    ket_qua = gia_tri_xa_nhat(L, x)
    print("Giá trị xa x nhất trong list là:", ket_qua)

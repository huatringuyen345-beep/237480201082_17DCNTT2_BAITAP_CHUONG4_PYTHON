def sap_xep_chan_khong_le(L):
    chan = []
    khong = []
    le = []

    for x in L:
        if x == 0:
            khong.append(x)
        elif x % 2 == 0:
            chan.append(x)
        else:
            le.append(x)

    return chan + khong + le


if __name__ == "__main__":

    L = []
    while True:
        try:
            n = int(input("Nhập số lượng phần tử: "))
            break
        except ValueError:
            print("Nhập số hợp lệ!")

    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhập phần tử thứ {i + 1}: "))
                L.append(x)
                break
            except ValueError:
                print("Nhập số nguyên hợp lệ!")

    # Gọi hàm
    ket_qua = sap_xep_chan_khong_le(L)
    print("List sau khi sắp xếp:", ket_qua)

def sap_xep_tang(L):
    """Hàm sắp xếp danh sách L theo thứ tự tăng dần và trả về danh sách."""
    L.sort()
    return L
if __name__ == "__main__":
    L = []
    while True:
        try:
            n = int(input("Nhập số lượng phần tử: "))
            break
        except ValueError:
            print("Nhập số bất kỳ!")

    # Nhập các phần tử
    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhập phần tử thứ {i + 1}: "))
                L.append(x)
                break
            except ValueError:
                print("Nhập số nguyên hợp lệ!")

    # Gọi hàm
    L = sap_xep_tang(L)
    print("List sau khi sắp xếp:", L)

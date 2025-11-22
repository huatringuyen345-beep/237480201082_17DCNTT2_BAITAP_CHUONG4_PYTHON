def tim_vi_tri(L):
    for i in range(1, len(L) - 1):
        if L[i] == L[i - 1] * L[i + 1]:
            return i + 1  # đổi sang vị trí 1-based
    return -1


if __name__ == "__main__":
    L = []
    while True:
        try:
            n = int(input("Nhập số lượng phần tử: "))
            break
        except ValueError:
            print("Nhập số bất kỳ!")

    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhập phần tử thứ {i + 1}: "))
                L.append(x)
                break
            except ValueError:
                print("Nhập số nguyên hợp lệ!")

    # Gọi hàm
    vi_tri = tim_vi_tri(L)
    print("Vị trí tìm được là:", vi_tri)

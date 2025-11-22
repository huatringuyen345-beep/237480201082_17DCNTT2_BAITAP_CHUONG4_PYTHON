def kiem_tra_tang(L):
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            return False
    return True


if __name__ == "__main__":
    L = []
    while True:
        try:
            n = int(input("Nhập số lượng phần tử: "))
            break
        except ValueError:
            print("Nhập số bất kỳ!")

    # Nhập danh sách
    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhập phần tử thứ {i+1}: "))
                L.append(x)
                break
            except ValueError:
                print("Nhập số nguyên hợp lệ!")

    # Gọi hàm kiểm tra
    is_sorted = kiem_tra_tang(L)
    print(is_sorted)

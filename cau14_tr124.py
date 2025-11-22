def so_duong_dau_tien(L):

    for x in L:
        if x > 0:
            return x
    return -1

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Nhập n: "))
            break
        except ValueError:
            print("Vui lòng nhập số nguyên!")


    L = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        L.append(x)

    kq = so_duong_dau_tien(L)
    print("Giá trị dương đầu tiên là:", kq)

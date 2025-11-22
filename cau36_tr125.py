def tim_sinh_vien(sv_list, ten_can_tim):
    for ten in sv_list:
        if ten.lower() == ten_can_tim.lower():
            return True
    return False


if __name__ == "__main__":
    print("Bấm 0 để thoát!")

    while True:
        try:
            n = int(input("Nhập số lượng sinh viên: "))
            break
        except ValueError:
            print("Nhập số hợp lệ!")

    # Nhập danh sách sinh viên
    sv = []
    for i in range(n):
        name = input(f"Nhập tên sinh viên thứ {i+1}: ")
        sv.append(name)

    # Tìm kiếm sinh viên
    while True:
        tim = input("Nhập tên sinh viên cần tìm (nhập 0 để dừng): ")
        if tim == "0":
            print("Kết thúc tìm kiếm!")
            break

        if tim_sinh_vien(sv, tim):
            print("=> Sinh viên có trong danh sách!")
        else:
            print("=> Không tìm thấy sinh viên!")

def chuoi(a,b):
    ket_qua = " "
    i = 0
    # trong khi i < diem so ky tu tron chuoi a
    while i<len(a):
        #neu trong a co tong  tai chuoi b
        if a[i:i+len(b)] == b:
            i += len(b) # bỏ qua chuỗi b
        else:
            ket_qua += a[i]
            i += 1
    print (f" Chuỗi sau khi xóa b khỏi a:{ket_qua}")
if __name__ == '__main__':
    a = input(" Nhập vào chuỗi a:")
    b = input(" Nhập vào chuỗi b:")
    chuoi(a,b)
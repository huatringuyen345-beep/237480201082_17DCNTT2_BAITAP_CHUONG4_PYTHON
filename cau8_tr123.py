
import string
def matkhau(mk):
    in_hoa = 0
    in_thuong = 0
    so = 0
    ky_tu_dac_biet = 0
    doi_dai_hop_le = 0
    for c in mk:
        if c.isupper():
                in_hoa += 1
        elif c.islower():
                in_thuong += 1
        elif c.isdigit():
                so += 1
        elif c in string.punctuation:
            ky_tu_dac_biet += 1


        doi_dai_hop_le = len(mk) > 6


    if in_hoa > 0 and in_thuong > 0 and so > 0 and ky_tu_dac_biet > 0 and doi_dai_hop_le:
        print("Mật khẩu mạnh")
    else:
        print("Mật khẩu yếu")


if __name__ == '__main__':
    mk = input("Nhập mật khẩu:")
    matkhau(mk)
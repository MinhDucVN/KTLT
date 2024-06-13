# Họ và tên sinh viên: Trần Minh Đức
# MSSV: 20216819

# Hàm tính a^d mod n bằng phương pháp lũy thừa bình phương
def modPow(a, d, n):
    result = 1
    a = a % n
    while d > 0:
        if d % 2 == 1:
            result = (result * a) % n
        d = d // 2
        a = (a * a) % n
    return result

# Lấy khóa bảo mật đã được tạo từ trước
fi = open("Data/PrivateKey.txt","r")
n = int(fi.readline())
a = int(fi.readline())
fi.close()

try:
    # Đọc bản mã là một số x thuộc Zn
    fi = open("Data/Ciphertext.txt","r")
    x = int(fi.readline())
except:
    print("Dữ liệu vào phải là 1 số nguyên dương!")
else:
    # Giãi mã và ghi bản giải mã vào file
    fo = open("Data/Plaintext_Decode.txt", "w")
    x = modPow(x, a, n)
    fo.write(str(x))
    fo.close()

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

# Lấy khóa công khai đã được tạo từ trước
fi = open("Data/PublicKey.txt","r")
n = int(fi.readline())
b = int(fi.readline())
fi.close()

try:
    # Đọc bản rõ là một số x thuộc Zn
    fi = open("Data/Plaintext.txt","r")
    x = int(fi.readline())
except:
    print("Dữ liệu vào phải là 1 số nguyên dương!")
else:
    # Mã hóa và ghi bản mã vào file
    fo = open("Data/Ciphertext.txt", "w")
    x = modPow(x, b, n)
    fo.write(str(x))
    fo.close()

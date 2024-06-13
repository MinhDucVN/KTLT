# Họ và tên sinh viên: Trần Minh Đức
# MSSV: 20216819

import math
import random

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


# Hàm kiểm tra tính nguyên tố thông dụng để tìm mảng sprime
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Hàm kiểm tra tính nguyên tố của một số nguyên lẻ n rất lớn bằng thuật toán Miller Rabin
def isPrimeMillerRabin(n):
    # Phân tích n - 1 = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    # Lấy ngẫu nhiên k số a trong mảng sprime
    k = min(n - 4, math.floor(2 * math.log(n) ** 2))
    if(k <= 1000):
        bases = sprime[0:k]
    else:
        bases = sprime
    # Kiểm tra từng số a trong danh sách
    for a in bases:
        x = modPow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for r in range(1, s):
            x = modPow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Hàm sinh số nguyên tố lớn N bits
def generatePrime(N):
    N = random.getrandbits(N)
    # Nếu N là số chẵn thì tăng lên 1 đơn vị
    if N % 2 == 0:
        N += 1
    # Lặp cho đến khi tìm được số nguyên tố
    while True:
        if isPrimeMillerRabin(N):
            return N
        else:
            N += 2

# Hàm xác định một số b bất kỳ sao cho ƯCLN(b, phi(n)) = 1
def getB(phi):
	b = 65537
	while True:
		if GCD(b, phi) == 1:
			break
		b+= 2
	return b

# Hàm xác định số a sao cho ab mod phi(n) = 1
def getA(b, phi):
	a = GCD_extended(b, phi)[0]
	if a < 0:
		a += phi
	return a

# Hàm lấy ƯCLN theo thuật toán Euclidean
def GCD(a, b):
	if b == 0:
		return a
	return GCD(b, a % b)

# Hàm xác định các thành phần của biểu thức ax + by = c; trả về x, y, c
# Thuật toán Euclidean mở rộng
def GCD_extended(a, b):
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, b
	while v3 != 0:
		q = u3//v3
		t1, t2, t3 = u1 - q*v1, u2 - q*v2, u3 - q*v3
		u1, u2, u3 = v1, v2, v3
		v1, v2, v3 = t1, t2, t3
	return u1, u2, u3

# Tạo mảng sprime
sprime = [2]
a = 3
while len(sprime) < 1000:
    if isPrime(a):
        sprime.append(a)
    a += 2
random.shuffle(sprime)

# Tạo số nguyên tố lớn 1024 bits
# p = generatePrime(1024)
# q = generatePrime(1024)
p = 61
q = 53
fo = open("Data/BigPrime.txt", "w")
fo.write(str(p)+'\n'+str(q))
fo.close()

# Tạo các khóa công khai n, b và khóa bảo mật a
n = p * q
phi = (p-1) * (q-1)
b = getB(phi)
a = getA(b, phi)
fo = open("Data/PublicKey.txt", "w")
fo.write(str(n)+'\n'+str(b))
fo.close()
fo = open("Data/PrivateKey.txt", "w")
fo.write(str(n)+'\n'+str(a))
fo.close()

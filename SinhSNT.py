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

# Hàm kiểm tra tính nguyên tố của một số nguyên lẻ n bằng thuật toán Miller Rabin
def isPrime(n):
    # Số nhỏ hơn 2 không phải số nguyên tố
    if n < 2:
        return False
    # Phân tích n - 1 = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    # Lấy danh sách các số a để kiểm tra theo bảng sau:
    # https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
    if n < 2047:
        bases = [2]
    elif n < 1373653:
        bases = [2, 3]
    elif n < 9080191:
        bases = [31, 73]
    elif n < 25326001:
        bases = [2, 3, 5]
    elif n < 3215031751:
        bases = [2, 3, 5, 7]
    elif n < 4759123141:
        bases = [2, 7, 61]
    elif n < 1122004669633:
        bases = [2, 13, 23, 1662803]
    elif n < 2152302898747:
        bases = [2, 3, 5, 7, 11]
    elif n < 3474749660383:
        bases = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        bases = [2, 3, 5, 7, 11, 13, 17]
    else:
        # Nếu n quá lớn thì lấy ngẫu nhiên k số a trong đoạn [2, n - 2]
        k = min(n - 4, math.floor(2 * math.log(n) ** 2))
        bases = random.sample(range(2, n -2), k)
    
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

# Hàm sinh số nguyên tố lớn hơn N cho trước
def generatePrime(N):
    # Nếu N là số chẵn thì tăng lên 1 đơn vị
    if N % 2 == 0:
        N += 1
    # Lặp cho đến khi tìm được số nguyên tố
    while True:
        if isPrime(N):
            return N
        else:
            N += 2

#Đọc file
with open("Input.txt", 'r') as fin:
    N = int(fin.read())
P = generatePrime(N)
with open("Output.txt", 'w') as fout:
    fout.write(str(P))

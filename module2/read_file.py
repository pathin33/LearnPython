"""

Mục tiêu:
- Hiểu cách đọc nội dung file trong Python
- Phân biệt read(), readline(), readlines()
- Hiểu absolute path và relative path
- Thực hành đọc file theo nhiều cách khác nhau
"""

# =====================================================
# 1. Chuẩn bị file để test
# =====================================================
# Hãy tạo một file tên: sample.txt
# Nội dung ví dụ:
#
# The quick brown fox jumps over the lazy dog
# This is the second line
# This is the third line
# This is the fourth line


# =====================================================
# 2. Đọc TOÀN BỘ nội dung file bằng read()
# =====================================================
# read() → trả về toàn bộ nội dung file dưới dạng string

with open("sample.txt", mode="r") as file:
    data = file.read()
    print("---- read(): đọc toàn bộ file ----")
    print(data)


# =====================================================
# 3. Đọc một SỐ KÝ TỰ nhất định bằng read(n)
# =====================================================
# read(44) → đọc 44 ký tự đầu tiên của file

with open("sample.txt", mode="r") as file:
    data = file.read(44)
    print("---- read(44): đọc 44 ký tự đầu ----")
    print(data)


# =====================================================
# 4. Đọc MỘT DÒNG bằng readline()
# =====================================================
# readline() → trả về dòng đầu tiên của file (string)

with open("sample.txt", mode="r") as file:
    line = file.readline()
    print("---- readline(): đọc dòng đầu tiên ----")
    print(line)


# =====================================================
# 5. Đọc MỘT PHẦN của dòng bằng readline(n)
# =====================================================
# readline(10) → đọc 10 ký tự đầu của dòng đầu tiên

with open("sample.txt", mode="r") as file:
    line = file.readline(10)
    print("---- readline(10): 10 ký tự đầu ----")
    print(line)


# =====================================================
# 6. Đọc TOÀN BỘ file thành LIST bằng readlines()
# =====================================================
# readlines() → trả về list các dòng theo thứ tự

with open("sample.txt", mode="r") as file:
    lines = file.readlines()
    print("---- readlines(): trả về list ----")
    print(lines)


# =====================================================
# 7. Duyệt từng dòng bằng for loop (từ readlines)
# =====================================================

with open("sample.txt", mode="r") as file:
    lines = file.readlines()
    print("---- Duyệt từng dòng ----")
    for line in lines:
        print(line)


# =====================================================
# 8. Cách hay hơn: duyệt trực tiếp file object
# =====================================================
# Khi dùng with open(), file có thể iterable trực tiếp

with open("sample.txt", mode="r") as file:
    print("---- Duyệt trực tiếp file ----")
    for line in file:
        print(line)


# =====================================================
# 9. Absolute path vs Relative path
# =====================================================
"""
ABSOLUTE PATH:
- Chứa đầy đủ đường dẫn từ gốc
- Ví dụ:
  Linux / Mac:
    /home/user/documents/sample.txt
  Windows:
    C:\\Users\\User\\Documents\\sample.txt

RELATIVE PATH:
- Dựa trên thư mục hiện tại
- Ví dụ:
    sample.txt
    data/sample.txt
"""

# Ví dụ absolute path (minh họa, không cần chạy)
# with open("/home/user/sample.txt", "r") as file:
#     print(file.read())


# =====================================================
# 10. Tổng kết
# =====================================================
"""
read()        → đọc toàn bộ file (string)
read(n)       → đọc n ký tự
readline()    → đọc 1 dòng
readline(n)   → đọc n ký tự của 1 dòng
readlines()   → đọc toàn bộ file thành list
for line in file → cách Pythonic nhất
"""

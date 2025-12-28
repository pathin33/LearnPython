"""
Mục tiêu:
- Hiểu string là gì
- Biết cách khai báo string (1 dòng, nhiều dòng)
- Hiểu string là sequence (chuỗi ký tự)
- Biết truy cập ký tự bằng index
- Biết dùng len() để lấy độ dài chuỗi
"""

# ======================================
# 1. STRING LÀ GÌ?
# ======================================
# String là một chuỗi các ký tự (characters)
# Được đặt trong dấu nháy đơn ' ' hoặc nháy kép " "

a = "hello"
b = "hello"

print(a)
print(b)

# Cả hai cách đều hợp lệ, nên chọn 1 cách và dùng nhất quán


# ======================================
# 2. STRING 1 DÒNG
# ======================================

single_line = "This is a single line string"
print(single_line)


# ======================================
# 3. STRING NHIỀU DÒNG (DÙNG BACKSLASH \)
# ======================================
# Dùng \ để nối các dòng thành MỘT chuỗi

multi_line = "This is a multi \
line string example"

print(multi_line)
# Kết quả vẫn là 1 dòng


# ======================================
# 4. GÁN LẠI GIÁ TRỊ STRING
# ======================================
# String có thể được gán lại giá trị mới

name = "John"
print(name)

name = "Paul"
print(name)


# ======================================
# 5. NỐI CHUỖI (STRING CONCATENATION)
# ======================================
# Dùng dấu + để nối chuỗi

x = "Hello "
y = "there"

print(x + y)  # Hello there


# ======================================
# 6. STRING LÀ SEQUENCE (CHUỖI CÓ THỨ TỰ)
# ======================================
# String là một sequence (giống mảng)
# Có thể truy cập từng ký tự bằng index
# Python dùng ZERO-INDEX (bắt đầu từ 0)

name = "John"

print(name[0])  # J (ký tự đầu tiên)
print(name[1])  # o
print(name[2])  # h
print(name[3])  # n


# ======================================
# 7. KIỂM TRA ĐỘ DÀI CHUỖI (len)
# ======================================
# len() trả về số lượng ký tự trong chuỗi

print(len(name))  # 4


# ======================================
# 8. TỔNG KẾT
# ======================================
"""
- String là chuỗi ký tự
- Khai báo bằng ' ' hoặc " "
- Có thể viết 1 dòng hoặc nhiều dòng
- Có thể nối chuỗi bằng +
- String là sequence → truy cập bằng index
- Dùng len() để biết độ dài chuỗi
"""

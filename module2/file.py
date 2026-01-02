"""
Mục tiêu:
- Hiểu cách làm việc với file trong Python
- Sử dụng open() và close()
- Sử dụng with open() (khuyến nghị)
- Đọc file ở dạng text và binary
"""

# =====================================================
# 1. Giới thiệu chung
# =====================================================
# Python cung cấp các hàm built-in để làm việc với file
# Các thao tác cơ bản:
# - Mở file
# - Đọc file
# - Ghi file
# - Đóng file
#
# Hai hàm quan trọng:
# - open()
# - close()


# =====================================================
# 2. Các mode mở file trong Python
# =====================================================
"""
r   : đọc file (text - mặc định)
rb  : đọc file (binary)
r+  : đọc + ghi
w   : ghi file (ghi đè nội dung cũ)
a   : append (ghi thêm vào cuối file)
b   : dùng kèm với r/w/a để xử lý binary
"""


# =====================================================
# 3. Mở file bằng open() và đóng bằng close()
# =====================================================

# Trước tiên, hãy tạo file test.txt với nội dung:
# Hello there

file = open("test.txt", mode="r")   # mở file để đọc (text)

data = file.readline()              # đọc 1 dòng trong file
print(data)                          # in nội dung file

file.close()                         # đóng file (bắt buộc)


# =====================================================
# 4. Vì sao phải close file?
# =====================================================
"""
- Giải phóng bộ nhớ
- Tránh lỗi truy cập file
- Tránh rò rỉ tài nguyên
"""


# =====================================================
# 5. Cách tốt hơn: dùng with open()
# =====================================================
# with open() sẽ:
# - Tự động đóng file
# - Xử lý exception tốt hơn
# - Được khuyến nghị sử dụng

with open("test.txt", mode="r") as file:
    data = file.readline()
    print(data)

# Không cần gọi file.close()


# =====================================================
# 6. Đọc nhiều dòng trong file
# =====================================================

with open("test.txt", mode="r") as file:
    lines = file.readlines()   # trả về list các dòng
    print(lines)


# =====================================================
# 7. Làm việc với file binary
# =====================================================
"""
- File text: con người đọc được
- File binary: không đọc trực tiếp được (ảnh, video, pdf...)
- Binary gọn hơn → hiệu năng tốt hơn
"""

# Ví dụ mở file ở dạng binary (minh họa, không cần test.txt)
# with open("image.png", "rb") as file:
#     data = file.read()


# =====================================================
# 8. Tổng kết kiến thức
# =====================================================
"""
- open(filename, mode) → mở file
- close() → đóng file
- readline() → đọc 1 dòng
- readlines() → đọc nhiều dòng
- with open() → cách dùng tốt nhất
- Text là mặc định, thêm 'b' để dùng binary
"""

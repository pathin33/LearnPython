"""
CHỦ ĐỀ: CHUYỂN ĐỔI KIỂU DỮ LIỆU TRONG PYTHON

Mục tiêu:
- Hiểu typecasting là gì
- Phân biệt implicit và explicit type conversion
- Biết cách chuyển đổi kiểu bằng các hàm Python
- Hiểu khi nào chuyển được, khi nào gây lỗi
"""

# ======================================
# 1. TYPECASTING LÀ GÌ?
# ======================================
# Typecasting là quá trình chuyển đổi
# dữ liệu từ kiểu này sang kiểu khác


# ======================================
# 2. IMPLICIT TYPE CONVERSION
# (CHUYỂN KIỂU NGẦM ĐỊNH)
# ======================================
# Python tự động chuyển kiểu để tránh mất dữ liệu

a = 10  # int
b = 2.5  # float

result = a + b  # int + float → float

print(result)
print(type(result))  # <class 'float'>

# Python đã tự động chuyển int → float


# ======================================
# 3. KIỂU KHÔNG TƯƠNG THÍCH → LỖI
# ======================================
# int và float → tương thích
# string và int → KHÔNG tương thích

x = "10"
y = 5

# Dòng dưới đây sẽ gây lỗi nếu bỏ comment
# print(x + y)

# TypeError: can only concatenate str (not "int") to str


# ======================================
# 4. EXPLICIT TYPE CONVERSION
# (CHUYỂN KIỂU TƯỜNG MINH)
# ======================================
# Developer chủ động chuyển kiểu
# bằng các hàm có sẵn của Python


# ===== str() =====
# Chuyển bất kỳ kiểu nào thành string

num = 100
text = str(num)

print(text)
print(type(text))  # <class 'str'>


# ===== int() =====
# Chuyển sang số nguyên

a = "20"
b = int(a)

print(b)
print(type(b))  # <class 'int'>


# ===== float() =====
# Chuyển sang số thực

c = "3.14"
d = float(c)

print(d)
print(type(d))  # <class 'float'>


# ======================================
# 5. VÍ DỤ THỰC TẾ (FORM NGƯỜI DÙNG)
# ======================================
# Dữ liệu nhập từ form luôn là STRING

user_age = "18"

# Cần chuyển sang int để tính toán
age = int(user_age)

print(age + 2)  # 20


# ======================================
# 6. MỘT SỐ HÀM TYPECASTING KHÁC
# ======================================

# ord(): trả về mã Unicode của ký tự
print(ord("A"))  # 65

# hex(): đổi số nguyên sang chuỗi hex
print(hex(255))  # 0xff

# oct(): đổi số nguyên sang chuỗi octal
print(oct(8))  # 0o10


# ======================================
# 7. CHUYỂN ĐỔI COLLECTION (GIỚI THIỆU)
# ======================================

lst = [1, 2, 3]

print(tuple(lst))  # list → tuple
print(set(lst))  # list → set


# ======================================
# 8. TỔNG KẾT
# ======================================
"""
- Typecasting là chuyển đổi kiểu dữ liệu
- Python có 2 loại:
  + Implicit: Python tự làm
  + Explicit: lập trình viên chủ động
- Dùng các hàm: str(), int(), float()
- Chỉ chuyển được khi kiểu dữ liệu tương thích
"""

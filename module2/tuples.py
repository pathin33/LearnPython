"""
Mục đích:
- Giải thích Tuple trong Python
- Cách khai báo tuple
- Truy cập phần tử bằng index
- Các phương thức của tuple
- Duyệt tuple bằng vòng lặp
- Hiểu rõ tính IMMUTABLE (bất biến) của tuple
"""

# =========================
# 1. TUPLE LÀ GÌ?
# =========================
# Tuple là một cấu trúc dữ liệu dạng SEQUENCE
# - Có thứ tự
# - Có thể chứa nhiều kiểu dữ liệu khác nhau
# - Quan trọng nhất: IMMUTABLE (không thể thay đổi)


# =========================
# 2. KHAI BÁO TUPLE
# =========================

my_tuple = (1, "strings", 4.5, True)

print(my_tuple)

# Có thể khai báo tuple không cần dấu ()
# Nhưng BEST PRACTICE là nên dùng ()
my_tuple2 = 1, "strings", 4.5, True
print(my_tuple2)


# =========================
# 3. TRUY CẬP PHẦN TỬ TRONG TUPLE
# =========================
# Index luôn bắt đầu từ 0

print(my_tuple[0])  # 1
print(my_tuple[1])  # "strings"


# =========================
# 4. KIỂM TRA KIỂU DỮ LIỆU
# =========================

print(type(my_tuple))
# <class 'tuple'>


# =========================
# 5. PHƯƠNG THỨC CỦA TUPLE
# =========================

# count(): đếm số lần xuất hiện của một giá trị
print(my_tuple.count("strings"))  # 1

# index(): trả về index của giá trị
print(my_tuple.index(4.5))  # 2


# =========================
# 6. DUYỆT TUPLE (ITERATE)
# =========================

for x in my_tuple:
    print("Value:", x)


# =========================
# 7. TÍNH IMMUTABLE CỦA TUPLE
# =========================
# Tuple KHÔNG thể thay đổi giá trị sau khi tạo

# DÒNG CODE DƯỚI ĐÂY SẼ BÁO LỖI
# my_tuple[0] = 5

"""
Lỗi nhận được:
TypeError: 'tuple' object does not support item assignment

→ Điều này chứng minh tuple là IMMUTABLE
"""


# =========================
# 8. SO SÁNH NHANH LIST & TUPLE
# =========================
"""
LIST:
- Mutable (có thể thay đổi)
- append, insert, remove được
- Chậm hơn tuple

TUPLE:
- Immutable (không thể thay đổi)
- An toàn hơn
- Nhanh hơn
- Dùng khi dữ liệu KHÔNG cần chỉnh sửa
"""

"""
FILE: data_types_overview.py
CHỦ ĐỀ: CÁC KIỂU DỮ LIỆU TRONG PYTHON

Mục tiêu:
- Hiểu data type là gì
- Nhận biết 5 nhóm kiểu dữ liệu chính trong Python
- Biết cách kiểm tra kiểu dữ liệu bằng type()
"""
# ==============================
# 1. NUMERIC DATA TYPES (KIỂU SỐ)
# ==============================

# Integer (số nguyên)
a = 10
print("a =", a, "->", type(a))  # <class 'int'>

# Float (số thực – có dấu thập phân)
b = 2.3
print("b =", b, "->", type(b))  # <class 'float'>

# Complex (số phức)
c = 10 + 5j
print("c =", c, "->", type(c))  # <class 'complex'>


# ==================================
# 2. SEQUENCE DATA TYPES (KIỂU DÃY)
# ==================================

# String (chuỗi ký tự)
s = "Hello Python"
print("s =", s, "->", type(s))  # <class 'str'>

# List (danh sách – có thể thay đổi)
lst = [1, 2, 3, "A", 4.5]
print("lst =", lst, "->", type(lst))  # <class 'list'>

# Truy cập phần tử bằng index
print("lst[0] =", lst[0])  # 1

# Tuple (giống list nhưng KHÔNG thay đổi được)
t = (1, 2, 3)
print("t =", t, "->", type(t))  # <class 'tuple'>


# =========================
# 3. DICTIONARY (TỪ ĐIỂN)
# =========================

# Dictionary lưu dữ liệu dạng key : value
ed = {"a": 22, "b": 44.4}

print("ed =", ed, "->", type(ed))  # <class 'dict'>

# Truy cập giá trị thông qua key
print("ed['a'] =", ed["a"])  # 22


# ======================
# 4. BOOLEAN (ĐÚNG / SAI)
# ======================

x = True
y = False

print("x =", x, "->", type(x))  # <class 'bool'>
print("y =", y, "->", type(y))  # <class 'bool'>

# Boolean thường dùng trong điều kiện
print("10 > 5 ->", 10 > 5)  # True
print("3 == 5 ->", 3 == 5)  # False


# =================
# 5. SET (TẬP HỢP)
# =================

# Set không có thứ tự và không cho phép trùng lặp
example_set = {1, 2, 3, 3, 4}

print("example_set =", example_set)
print("type =", type(example_set))  # <class 'set'>


# ==========================================
# 6. PYTHON TỰ ĐỘNG GÁN KIỂU DỮ LIỆU
# ==========================================

p = 100  # int
q = 5.6  # float
r = "Python"  # str
s = [1, 2, 3]  # list

print("\nPython tự động gán kiểu dữ liệu:")
print("p ->", type(p))
print("q ->", type(q))
print("r ->", type(r))
print("s ->", type(s))
"""
TỔNG KẾT:
- Python có nhiều kiểu dữ liệu khác nhau
- Không cần khai báo kiểu, Python tự gán
- Dùng type() để kiểm tra kiểu dữ liệu
- Hiểu data type giúp code đúng và ít lỗi hơn
"""

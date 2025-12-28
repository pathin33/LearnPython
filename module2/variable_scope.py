"""
Mục đích:
- Giải thích khái niệm Scope (phạm vi biến) trong Python
- Minh họa 4 loại scope theo quy tắc LEGB:
  Local, Enclosing, Global, Built-in
- Hiểu biến nào truy cập được ở đâu và vì sao
"""

# =========================
# 1. SCOPE LÀ GÌ?
# =========================
# Scope (phạm vi) xác định:
# - Biến được khai báo ở đâu
# - Biến có thể được truy cập ở đâu
#
# Mục đích:
# - Tránh thay đổi biến ngoài ý muốn
# - Giảm lỗi trong chương trình
#
# Python dùng quy tắc LEGB để tìm biến

# =========================
# 2. LEGB LÀ GÌ?
# =========================
"""
LEGB = thứ tự Python tìm biến

L - Local      : trong hàm hiện tại
E - Enclosing  : hàm bao bên ngoài (nested function)
G - Global     : biến khai báo ngoài cùng file
B - Built-in   : biến/hàm có sẵn của Python (print, len, def, ...)
"""


# =========================
# 3. GLOBAL SCOPE
# =========================
# Biến khai báo ngoài function → Global scope

my_global = 10


def fn1():
    # local_v = 5  # Local scope (chỉ tồn tại trong fn1)

    print("Access to global:", my_global)
    # fn1 có thể truy cập biến global


# Gọi hàm
fn1()

# print(local_v)
# ❌ Lỗi NameError
# Vì local_v chỉ tồn tại trong fn1


# =========================
# 4. LOCAL SCOPE
# =========================
# Biến được khai báo trong hàm
# → Chỉ dùng được trong hàm đó


def example_local():
    x = 100
    print("Local x:", x)


example_local()

# print(x)
# ❌ Lỗi: x không tồn tại ngoài hàm


# =========================
# 5. ENCLOSING SCOPE
# =========================
# Enclosing scope xuất hiện khi:
# - Có function lồng trong function


def fn_outer():
    enclosed_v = 8  # Enclosing scope

    def fn_inner():
        # local_inner = 3  # Local scope của fn_inner

        # fn_inner có thể truy cập:
        # - local_inner (local)
        # - enclosed_v (enclosing)
        # - my_global (global)
        print("Access to enclosed:", enclosed_v)
        print("Access to global:", my_global)

    fn_inner()  # Phải gọi thì fn_inner mới chạy


fn_outer()

# print(enclosed_v)
# ❌ Lỗi: enclosed_v không tồn tại bên ngoài fn_outer


# =========================
# 6. BUILT-IN SCOPE
# =========================
# Built-in scope là các hàm/keyword có sẵn của Python
# Ví dụ: print, len, type, input, def, range

print("Hello")  # print là built-in
print(len("Python"))  # len là built-in
print(type(123))  # type là built-in

# Built-in scope:
# - Có thể dùng ở mọi nơi
# - Trong global
# - Trong local
# - Trong enclosing


# =========================
# 7. TÓM TẮT QUAN TRỌNG
# =========================
"""
- Biến LOCAL không dùng được bên ngoài hàm
- Biến ENCLOSING dùng được trong hàm con
- Biến GLOBAL dùng được ở mọi nơi (nhưng nên hạn chế)
- BUILT-IN là các hàm có sẵn của Python

Quy tắc tìm biến:
Local → Enclosing → Global → Built-in

Global scope thường KHÔNG khuyến khích dùng nhiều
vì dễ gây lỗi và khó kiểm soát
"""

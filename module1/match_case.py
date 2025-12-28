"""
Mục đích:
- So sánh if / elif / else với match case
- Minh họa cách dùng match case (Python 3.10+)
- Ví dụ thực tế: xử lý HTTP status code
"""

# =========================
# 1. DÙNG IF / ELIF / ELSE
# =========================

# HTTP status code (mã trạng thái HTTP)
http_status = 200

if http_status == 200 or http_status == 201:
    print("Success")

elif http_status == 400:
    print("Bad Request")

elif http_status == 500 or http_status == 501:
    print("Server Error")

else:
    # Else là trường hợp mặc định
    print("Unknown")


# =========================
# 2. DÙNG MATCH CASE (Python 3.10+)
# =========================
# match case giúp code:
# - Gọn hơn
# - Dễ đọc hơn
# - Phù hợp khi có NHIỀU điều kiện

match http_status:
    case 200 | 201:
        # | có nghĩa là OR
        print("Success")

    case 400:
        print("Bad Request")

    case 500 | 501:
        print("Server Error")

    case _:
        # case _ tương đương với else
        print("Unknown")


# =========================
# 3. THỬ THAY ĐỔI GIÁ TRỊ
# =========================
# Bạn có thể đổi giá trị http_status để test:
#
# http_status = 201  -> Success
# http_status = 400  -> Bad Request
# http_status = 500  -> Server Error
# http_status = 550  -> Unknown


# =========================
# 4. TÓM TẮT KIẾN THỨC
# =========================
"""
IF / ELIF / ELSE:
- Phù hợp khi ít điều kiện
- Nhiều điều kiện -> code dài, khó đọc

MATCH CASE:
- Ra mắt từ Python 3.10
- So sánh 1 biến với NHIỀU giá trị
- Gọn, rõ ràng, dễ bảo trì

Cú pháp quan trọng:
- case 1 | 2 | 3  : OR
- case _          : default (else)
"""
